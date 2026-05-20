<!--
  AI-QA Sentinel Pro - Advanced Test Studio
  Repository: https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro
-->

<h1 align="center" style="color:#39FF14;font-family: 'Orbitron', monospace;">
  <img src="https://img.shields.io/badge/Cyberpunk-Neon-blueviolet?style=for-the-badge" alt="Cyberpunk Neon Badge"/><br>
  AI-QA Sentinel Pro<br>
  <sub>Advanced Cyberpunk Automation & AI-Driven Quality Audit Studio</sub>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-39FF14?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/AI-Gemini%202.5%20Flash-brightgreen?style=flat-square&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square">
</p>

---

## 🌃 Project Overview

**AI-QA Sentinel Pro** is an enterprise-grade, Cyberpunk/Neon-themed graphical automation studio purpose-built for advanced Android QA, stress testing, and security auditing. With a CustomTkinter interface and deep PPADB integration (Pure-Python ADB), it performs interactive device telemetry, stress tests, log auditing, and sandbox inspections—all while leveraging Google GenAI (`gemini-2.5-flash`) to deliver instant, actionable AI-powered Quality Audit Reports.

---

## 🦾 System Architecture & Components

| Component        | Description                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------|
| `main.py`        | Entry point. Initializes the application with custom neon UI styles and config.                                   |
| `gui.py`         | Central AppGUI. Runs asynchronous background loops for live device status and metrics display.                    |
| `engine.py`      | Hardware orchestration: maps PPADB clients, runs Monkey test routines, manages Logcat filtering, Gemini inference.|
| `adb_service.py` | Standalone service for bundling and auto-starting the internal ADB server, especially in packaged executables.    |
| `theme.py`       | Defines high-tech color schemes—Neon Blue, Cyber Purple, Success Green, Error Red—for a premium visual aesthetic. |

---

## 🧪 Verified Benchmarking Environment

This tool was engineered and benchmarked in the following environment:

| Layer           | Tested Equipment Profile                                |
| :-------------- | :----------------------------------------------------- |
| Workstation PC  | Intel Core i5-4460 (4th Generation) Desktop Processor  |
| Android Target  | OPPO A5 Physical Mobile Hardware Device                |

---

## 🚦 Standalone EXE API Key Configuration

> **🟢 For End-Users of the Standalone Executable (`main.exe`):**

- **No Python is required!**  
- To provide your [Gemini API Key](https://ai.google.dev/gemini-api/docs/get-api-key), simply:
  1. Create a plain text file named `.env` in the **same directory as your `main.exe`**.
  2. Paste your key as follows:
      ```
      GEMINI_API_KEY=your_actual_gemini_api_key_here
      ```
- On launch, the executable will auto-load `.env` and authenticate the AI reporting system.
- **You do not interact with any CLI environment layers; just double-click and operate.**

---

## 👨‍💻 Prerequisites & Developer Setup (Python Source)

- **Python:** 3.9+
- **pip:** Latest recommended
- **Dependencies:**
  - `ppadb` (Pure-Python ADB)
  - `customtkinter`
  - `google-generativeai`
  - `python-dotenv`

Install all requirements:

```bash
pip install -r requirements.txt
```

Create a `.env` file in your repo root:

```ini
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## 🗃️ Bundling the Application (PyInstaller)

Build a full-featured Windows executable (includes ADB):

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Run the bundler:**

    ```bash
    pyinstaller --add-data="adb_bin;adb_bin" --onefile main.py
    ```

    > - Ensure the `adb_bin` folder contains the OS-specific ADB binaries.
    > - The `--add-data` path follows the format for your OS (`;` on Windows, `:` on Linux/Mac).

---

## 🛠️ Core Functional Suites

| Suite                               | Description                                                                 |
|------------------------------------- |-----------------------------------------------------------------------------|
| 🚀 **Live Device Telemetry**          | Real-time tracking (CPU, RAM heap, battery temp) for any connected Android. |
| 🐒 **Monitored Monkey Suite**         | 60s randomized event injector, with live device metric mapping per event.   |
| 🛡️ **Deep Logcat Exception Scanner**  | Tail-parses logcat (`*:E`) for live package runtime exception spotting.     |
| 📦 **Sandbox Directory Inspector**    | Audits APK payload sizing, detects cache leaks, and boundary anomalies.     |
| 🤖 **Consolidated Master AI Report**  | Auto-ingests telemetry, composes executive DevOps actions via Gemini AI.    |

---

## 🎬 Project Demo Video

[![Watch the Demo](https://img.shields.io/badge/YouTube-Project%20Demo-red?logo=youtube&style=for-the-badge)](https://youtu.be/PzhZ1_om6Eo?si=iDkLGLEp-_dPEEU5)
<!-- Replace the above link with your actual walkthrough when available -->

---

## 📰 License

```
AI-QA Sentinel Pro is licensed under the
GNU General Public License v3.0 (GPL-3.0).
See the LICENSE file for details.
```
