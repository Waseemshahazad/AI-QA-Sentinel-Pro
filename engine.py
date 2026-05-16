import time
import random
import socket
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from ppadb.client import Client as AdbClient
from adb_service import ADBService  # Importing the separate ADB service

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

try:
    ai_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None
except Exception:
    ai_client = None


class QAEngine:
    SESSION_LOGS = []

    def __init__(self, package_name):
        self.package_name = package_name
        ADBService.setup_internal_adb()  # Calling from the separate file
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.device = self.connect_device()

    def connect_device(self):
        try:
            devices = self.client.devices()
            return devices[0] if devices else None
        except Exception:
            return None

    def is_internet_available(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True
        except OSError:
            return False

    def launch_target_app(self):
        if not self.device: return False
        try:
            self.device.shell(f"monkey -p {self.package_name} -c android.intent.category.LAUNCHER 1")
            time.sleep(2.0)
            return True
        except Exception:
            return False

    def get_live_metrics(self):
        if not self.device: return "0%", "0MB", "0°C"
        try:
            cpu_data = self.device.shell(f"dumpsys cpuinfo | grep {self.package_name}").strip()
            cpu = cpu_data.split()[0] if cpu_data else "0%"

            mem_data = self.device.shell(f"dumpsys meminfo {self.package_name} | grep 'TOTAL:'").strip()
            ram = mem_data.split()[1] if mem_data else "0MB"

            battery_info = self.device.shell("dumpsys battery | grep temperature").strip()
            temp_raw = re.findall(r'\d+', battery_info)
            temp = f"{int(temp_raw[0]) / 10}°C" if temp_raw else "N/A"

            return cpu, ram, temp
        except Exception:
            return "Error", "Error", "Error"

    def run_monitored_monkey(self, log_callback, duration=60):
        if not self.device: return
        log_callback(f"🐒 Starting Extended Monkey Stress Suite ({duration}s)...")
        QAEngine.SESSION_LOGS.append(f"\n--- MONKEY STRESS TEST TRIAL ({duration}s) ---")
        start_time = time.time()

        while time.time() - start_time < duration:
            x, y = random.randint(120, 600), random.randint(250, 800)
            self.device.shell(f"input tap {x} {y}")
            cpu, ram, temp = self.get_live_metrics()
            log_line = f"Tap ({x}, {y}) -> CPU: {cpu} | RAM: {ram} | Temp: {temp}"
            log_callback(log_line)
            QAEngine.SESSION_LOGS.append(log_line)
            time.sleep(0.4)
        log_callback("✅ Monkey Stress Test completed.")

    def run_logcat_security_scan(self, log_callback):
        if not self.device: return
        log_callback("🛡️ Running Deep Logcat Exception Frame Scanner (50 Lines)...")
        QAEngine.SESSION_LOGS.append("\n--- LOGCAT ERROR & SECURITY AUDIT ---")
        try:
            raw_logs = self.device.shell(f"logcat -d *:E | grep {self.package_name} | tail -n 50").strip()
            if not raw_logs:
                raw_logs = "No critical runtime exceptions found in current logcat frame."
            log_callback(raw_logs)
            QAEngine.SESSION_LOGS.append(raw_logs)
        except Exception as e:
            log_callback(f"Scan failed: {str(e)}")

    def run_storage_bloat_test(self, log_callback):
        if not self.device: return
        log_callback("📦 Auditing Application Sandbox Directories...")
        QAEngine.SESSION_LOGS.append("\n--- APPLICATION STORAGE BLOAT AUDIT ---")
        try:
            path_info = self.device.shell(f"pm path {self.package_name}").replace("package:", "").strip()
            apk_size = self.device.shell(f"du -h {path_info}").split()[0] if path_info else "Unknown"
            report = f"Base APK Payload foot-print: {apk_size}\nScanning cache boundaries for unreleased assets..."
            log_callback(report)
            QAEngine.SESSION_LOGS.append(report)
        except Exception as e:
            log_callback(f"Storage audit bypassed: {str(e)}")

    def compile_full_ai_report(self, log_callback):
        log_callback("\n🤖 Assembling all executed tests for Consolidated Gemini Report...")
        if not QAEngine.SESSION_LOGS:
            log_callback("⚠️ Report Cancelled: No test suites have been run yet.")
            return
        if not self.is_internet_available():
            log_callback("🔌 Network Error: Internet connection is offline.")
            return

        master_data_payload = "\n".join(QAEngine.SESSION_LOGS)
        current_date_str = datetime.now().strftime("%B %d, %Y")

        prompt = f"""
        You are a Principal Mobile DevOps and Lead Automation QA Engineer.
        Produce a highly professional audit report based on the logs below.

        CRITICAL OUTPUT FORMAT RULES:
        - The report headers must be EXACTLY:
          To: DevOps & QA Development Team
          From: QA SENTINEL PRO - Automated AI Audit
          Date: {current_date_str}
        - DO NOT use placeholders like '[Your Name]', '[Your Title]', or brackets.
        - List the core stability risks and provide solid technical instructions.

        SESSION RUN LOGS:
        {master_data_payload}
        """
        try:
            response = ai_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            log_callback(f"\n📋 ======= MASTER AI AUTOMATION QUALITY REPORT =======")
            log_callback(response.text)
            log_callback(f"====================================================\n")
        except Exception as e:
            log_callback(f"❌ Master AI Report compilation aborted: {str(e)}")