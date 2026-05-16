import os
import sys


class ADBService:
    @staticmethod
    def setup_internal_adb():
        """Finds and starts the bundled ADB from inside the EXE or project folder."""
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))

            adb_path = os.path.join(base_path, "adb_bin", "adb.exe")

            if os.path.exists(adb_path):
                os.system(f'"{adb_path}" start-server')
        except Exception:
            pass