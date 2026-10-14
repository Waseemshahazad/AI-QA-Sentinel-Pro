<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contributing to AI-QA Sentinel Pro</title>
</head>
<body>
    <h1>Contributing to AI-QA Sentinel Pro</h1>
    <p>Thank you for your interest in contributing to <strong>AI-QA Sentinel Pro</strong>! We welcome bug reports, feature requests, documentation improvements, and pull requests.</p>
    <p>Please follow these guidelines to make your contribution process smooth and effective, especially during events like <strong>Hacktoberfest</strong>.</p>
    
    <hr>

    <h2>🚀 Getting Started</h2>
    <ol>
        <li><strong>Fork</strong> the repository on GitHub: <a href="https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro">https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro</a></li>
        <li><strong>Clone</strong> your-forked repository to your local machine:
            <pre><code>git clone https://github.com/YOUR_USERNAME/AI-QA-Sentinel-Pro.git
cd AI-QA-Sentinel-Pro</code></pre>
        </li>
        <li><strong>Create a new branch</strong> for your feature or bugfix:
            <pre><code>git checkout -b feature/your-awesome-feature</code></pre>
        </li>
    </ol>

    <hr>

    <h2>🛠️ Local Development Setup</h2>
    <p>Ensure you have <strong>Python 3.9+</strong> installed on your system.</p>
    <ol>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Configure Environment Variables:</strong>
            <p>Create a <code>.env</code> file in the root directory of the project and add your Google Gemini API key:</p>
            <pre><code>GEMINI_API_KEY=your_actual_gemini_api_key_here</code></pre>
        </li>
        <li><strong>Run the Application:</strong>
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

    <hr>

    <h2>💡 How to Contribute</h2>
    <ul>
        <li><strong>Find an Issue:</strong> Look at the existing <a href="https://github.com/Waseemshahazad/AI-QA-Sentinel-Pro/issues">Issues</a> tab or create a new one to discuss your proposed changes.</li>
        <li><strong>Make Changes:</strong> Write clean, documented Python code adhering to the existing CustomTkinter UI and PPADB architecture.</li>
        <li><strong>Commit Changes:</strong> Use clear and descriptive commit messages:
            <pre><code>git commit -m "feat: add new device diagnostic metric"</code></pre>
        </li>
        <li><strong>Push and Open PR:</strong> Push your changes to your fork and open a Pull Request (PR) targeting the <code>main</code> branch.</li>
    </ul>

    <hr>

    <h2>🍂 Hacktoberfest Guidelines</h2>
    <ul>
        <li>Ensure your pull requests are meaningful and add value to the project (spam PRs will be marked as invalid/spam).</li>
        <li>Maintainers will review your code and label valid PRs with <code>hacktoberfest-accepted</code> where applicable.</li>
    </ul>

    <p>Thank you for helping improve AI-QA Sentinel Pro!</p>
</body>
</html>
