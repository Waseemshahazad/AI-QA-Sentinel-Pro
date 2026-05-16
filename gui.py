import customtkinter as ctk
import threading
import time
import os
from theme import NEON_BLUE, CYBER_PURPLE, DARK_BG, SIDEBAR_BG, SUCCESS_GREEN
from engine import QAEngine

CONFIG_FILE = "config.txt"


class AppGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI-QA SENTINEL PRO - Advanced Test Studio")
        self.geometry("1020x760")
        self.configure(fg_color=DARK_BG)

        # Centralized master engine instance to prevent multiple connections and flickering
        self.engine = None
        self.last_pkg = None

        self.setup_ui()
        self.load_saved_package()
        self.start_metrics_loop()

    def setup_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=240, fg_color=SIDEBAR_BG, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.title_lbl = ctk.CTkLabel(self.sidebar, text="QA SENTINEL", text_color=NEON_BLUE,
                                      font=("Orbitron", 24, "bold"))
        self.title_lbl.pack(pady=30)

        self.dash_frame = ctk.CTkFrame(self.sidebar, fg_color="#141414", border_color="#222222", border_width=1,
                                       corner_radius=8)
        self.dash_frame.pack(pady=20, padx=15, fill="x")

        self.dash_title = ctk.CTkLabel(self.dash_frame, text="LIVE DEVICE STATUS", text_color=CYBER_PURPLE,
                                       font=("Arial", 12, "bold"))
        self.dash_title.pack(pady=5)

        self.cpu_lbl = ctk.CTkLabel(self.dash_frame, text="CPU Usage: 0%", text_color="#ffffff", font=("Consolas", 12))
        self.cpu_lbl.pack(pady=2)

        self.ram_lbl = ctk.CTkLabel(self.dash_frame, text="RAM Heap: 0MB", text_color="#ffffff", font=("Consolas", 12))
        self.ram_lbl.pack(pady=2)

        self.temp_lbl = ctk.CTkLabel(self.dash_frame, text="Device Temp: 0°C", text_color="#ffffff",
                                     font=("Consolas", 12))
        self.temp_lbl.pack(pady=2)

        self.ver_lbl = ctk.CTkLabel(self.sidebar, text="V3.6 Architecture Build", text_color="#555555",
                                    font=("Arial", 11, "italic"))
        self.ver_lbl.pack(side="bottom", pady=20)

        self.pkg_entry = ctk.CTkEntry(self, placeholder_text="Enter Android Target Package Name...", width=520,
                                      border_color=NEON_BLUE, font=("Consolas", 13))
        self.pkg_entry.pack(pady=20)

        self.console = ctk.CTkTextbox(self, width=740, height=340, fg_color="#000000", text_color=NEON_BLUE,
                                      font=("Consolas", 12), border_color="#222222", border_width=1)
        self.console.pack(pady=5, padx=20)

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.launch_btn = ctk.CTkButton(self.btn_frame, text="🚀 LAUNCH APP TARGET", fg_color=CYBER_PURPLE,
                                        hover_color="#b336ff", text_color="#ffffff", width=680, height=38,
                                        font=("Arial", 12, "bold"), command=lambda: self.trigger_test("launch"))
        self.launch_btn.grid(row=0, column=0, columnspan=3, pady=10)

        self.monkey_btn = ctk.CTkButton(self.btn_frame, text="🐒 RUN MONKEY TEST (60s)", fg_color="#1c1c1c",
                                        hover_color="#2b2b2b", text_color="#ffffff", border_color=NEON_BLUE,
                                        border_width=1, width=220, height=36, font=("Arial", 11, "bold"),
                                        command=lambda: self.trigger_test("monkey"))
        self.monkey_btn.grid(row=1, column=0, padx=10, pady=6)

        self.security_btn = ctk.CTkButton(self.btn_frame, text="🛡️ RUN DEEP LOGCAT SCAN", fg_color="#1c1c1c",
                                          hover_color="#2b2b2b", text_color="#ffffff", border_color=NEON_BLUE,
                                          border_width=1, width=220, height=36, font=("Arial", 11, "bold"),
                                          command=lambda: self.trigger_test("logcat"))
        self.security_btn.grid(row=1, column=1, padx=10, pady=6)

        self.bloat_btn = ctk.CTkButton(self.btn_frame, text="📦 RUN BLOat INSPECTION", fg_color="#1c1c1c",
                                       hover_color="#2b2b2b", text_color="#ffffff", border_color=NEON_BLUE,
                                       border_width=1, width=220, height=36, font=("Arial", 11, "bold"),
                                       command=lambda: self.trigger_test("bloat"))
        self.bloat_btn.grid(row=1, column=2, padx=10, pady=6)

        self.report_btn = ctk.CTkButton(self, text="🤖 GENERATE CONSOLIDATED AI REPORT", fg_color=SUCCESS_GREEN,
                                        hover_color="#2fd115", text_color="#000000", width=680, height=45,
                                        font=("Arial", 13, "bold"), command=self.trigger_master_report)
        self.report_btn.pack(pady=15)

    def append_log(self, message):
        self.console.insert("end", f"> {message}\n")
        self.console.see("end")

    def get_pkg(self):
        pkg = self.pkg_entry.get().strip()
        if pkg:
            self.save_package_name(pkg)
            return pkg
        return None

    def load_saved_package(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    saved_pkg = f.read().strip()
                    if saved_pkg:
                        self.pkg_entry.insert(0, saved_pkg)
            except Exception:
                pass

    def save_package_name(self, pkg):
        try:
            with open(CONFIG_FILE, "w") as f:
                f.write(pkg)
        except Exception:
            pass

    def update_engine_instance(self, pkg):
        """Safely syncs and updates the single master engine reference."""
        if self.engine is None or pkg != self.last_pkg:
            self.engine = QAEngine(pkg)
            self.last_pkg = pkg
        return self.engine

    def start_metrics_loop(self):
        def loop():
            while True:
                try:
                    pkg = self.pkg_entry.get().strip()
                    if pkg:
                        # Synchronize with the main master engine instance
                        engine = self.update_engine_instance(pkg)

                        if engine and engine.device:
                            cpu, ram, temp = engine.get_live_metrics()

                            # Explicitly format string conversion to guarantee CPU rendering on the UI
                            self.cpu_lbl.configure(text=f"CPU Usage: {str(cpu).strip()}")
                            self.ram_lbl.configure(text=f"RAM Heap: {ram}")
                            self.temp_lbl.configure(text=f"Device Temp: {temp}")
                except Exception:
                    pass
                time.sleep(2)

        threading.Thread(target=loop, daemon=True).start()

    def trigger_test(self, test_type):
        pkg = self.get_pkg()
        if pkg:
            # Force engine sync prior to launching background thread tests
            self.update_engine_instance(pkg)
            threading.Thread(target=self.run_selected_test, args=(pkg, test_type), daemon=True).start()

    def trigger_master_report(self):
        pkg = self.get_pkg()
        if pkg:
            self.update_engine_instance(pkg)
            threading.Thread(target=self.run_master_report, args=(pkg,), daemon=True).start()

    def run_selected_test(self, package, test_type):
        if not self.engine or not self.engine.device:
            self.append_log("CRITICAL: ADB Device missing.")
            return

        if test_type == "launch":
            self.append_log(f"Booting target package: {package} ...")
            if self.engine.launch_target_app():
                self.append_log("🚀 Target launched successfully.")
            else:
                self.append_log("❌ Launch request failed.")
        elif test_type == "monkey":
            self.engine.run_monitored_monkey(self.append_log)
        elif test_type == "logcat":
            self.engine.run_logcat_security_scan(self.append_log)
        elif test_type == "bloat":
            self.engine.run_storage_bloat_test(self.append_log)

    def run_master_report(self, package):
        if self.engine:
            self.engine.compile_full_ai_report(self.append_log)


if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()