# Contributing to AI-QA Sentinel Pro

Thank you for your interest in contributing to AI-QA Sentinel Pro! We welcome bug reports, feature requests, documentation improvements, and pull requests.

Please follow these guidelines to make your contribution process smooth and effective, especially during events like Hacktoberfest.

---

## 🚀 Getting Started

1. Fork the repository on GitHub:
   - Repository: https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro

2. Clone your fork to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/AI-QA-Sentinel-Pro.git
cd AI-QA-Sentinel-Pro
```

3. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-awesome-feature
```

---

## 🛠️ Local Development Setup

Ensure you have Python 3.9+ installed on your system.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure environment variables:

Create a `.env` file in the root directory of the project and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

3. Run the application:

```bash
python main.py
```

---

## 💡 How to Contribute

- Find an issue: check the existing [Issues](https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro/issues) tab or create a new one to discuss your proposed changes.
- Make changes: write clean, documented Python code that follows the existing CustomTkinter UI and PPADB architecture.
- Commit changes: use clear and descriptive commit messages.

```bash
git commit -m "feat: add new device diagnostic metric"
```

- Push and open a pull request: push your changes to your fork and open a Pull Request (PR) targeting the `main` branch.

---

## 🍂 Hacktoberfest Guidelines

- Ensure your pull requests are meaningful and add value to the project. Spam PRs will be marked as invalid or spam.
- Maintainers will review your code and label valid PRs with `hacktoberfest-accepted` where applicable.

Thank you for helping improve AI-QA Sentinel Pro!
