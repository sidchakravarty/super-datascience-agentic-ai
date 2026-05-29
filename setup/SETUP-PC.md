# 🚀 Agentic AI Course Setup Guide (Windows)

Hellooooo everyone! Ready to get your Agentic AI environment up and running on Windows? Follow this step-by-step guide and you’ll be coding agents in no time. Let’s dive in!

---

## 1. Pre-requisites

Before we get started, let’s make sure you have all the right tools:

### a. Download and Install Git

- [Git for Windows](https://git-scm.com/download/win)
- Run the installer and follow the prompts. (Default options are fine!)

### b. Download and Install UV

- [UV Installer](https://docs.astral.sh/uv/getting-started/installation/)
- Verify install:
  ```powershell
  uv --version
  ```

### c. Download and Install an IDE

- [Cursor](https://www.cursor.com/) or [VS Code](https://code.visualstudio.com/)
- Download, install, and open your favorite editor.

---

## 2. GitHub Repo Setup

Let’s grab the course materials!

### a. Fork the Repo

- Go to [Agentic AI GitHub Repo](https://github.com/SuperDataScience-Community/agentic-ai)
- Click **Fork** (top right) to create your own copy.

### b. Clone to Your Machine

- Open your terminal (PowerShell or Command Prompt).
- Navigate to your projects directory:
  ```powershell
  cd C:\Users\<your-username>\Projects
  ```
- Clone your forked repo:
  ```powershell
  git clone https://github.com/<your-github-username>/agentic-ai.git
  ```
- Enter the repo folder:
  ```powershell
  cd agentic-ai
  ```

---

## 3. Setup Environment Using UV

Time to install dependencies and set up your virtual environment!

- In the repo directory, run:
  ```powershell
  uv sync
  ```
- This creates a virtual environment and installs all required packages from `requirements.txt` and `environment.yaml`.

<div style="border-radius:16px;background:#3b1c1c;margin:1em 0;padding:1em 1em 1em 3em;color:#eceff4;position:relative;box-shadow:0 6px 16px rgba(0,0,0,.4)">
  <b style="color:#bf616a;font-size:1.25em">Warning:</b>
  <ul style="margin:.6em 0 0;padding-left:1.2em;line-height:1.6">
    <li>If you see an error like <code>activate : File ... cannot be loaded because running scripts is disabled on this system</code>, PowerShell is blocking script execution by default.</li>
    <li>To fix this:
      <ol>
        <li>Open PowerShell as administrator.</li>
        <li>Run <code>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser</code></li>
        <li>Close and re-open PowerShell (restart your machine if needed).</li>
        <li>Try activating your environment again by navigating to your project folder and running <code>uv sync</code> again</li>
      </ol>
    </li>
    <li>For more info, see <a href="https://go.microsoft.com/fwlink/?LinkID=135170">about_Execution_Policies</a>.</li>
  </ul>
  <div style="position:absolute;top:-.8em;left:-.8em;width:2.4em;height:2.4em;border-radius:50%;background:#bf616a;color:#2e3440;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.2em">⚠️</div>
</div>

---

## 4. Setup Environment Variables

You’ll need API keys for OpenAI, Gemini, and Anthropic. Here’s how:

### a. Get Your API Keys

- [OpenAI](https://platform.openai.com/api-keys)
- [Anthropic](https://console.anthropic.com/settings/keys)
- [Gemini](https://aistudio.google.com/app/apikey)

### b. Store Keys in `.env` File

- Open `.env` in your editor and paste your API keys:
  ```env
  OPENAI_API_KEY=sk-...
  GEMINI_API_KEY=...
  ANTHROPIC_API_KEY=...
  ```

---

That's a wrap for your Windows setup, ladies and gentlemen 🎉 Now it's your turn — I really can't wait to see what you build!
