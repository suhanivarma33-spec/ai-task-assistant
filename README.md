# Taskmate — Full-stack task manager

A small full-stack web app built with Python, Flask, SQLite, HTML, CSS, and JavaScript. It lets you add tasks, choose a priority, mark tasks complete, delete tasks, and get a simple task breakdown from a built-in demo helper.

## Features

- Add tasks with optional details and priority
- Mark tasks complete or incomplete
- Delete tasks
- Store tasks in a local SQLite database
- Get a short suggested plan without an API key
- Responsive layout for desktop and mobile

> The task suggestion is a local demo helper, not an OpenAI-powered response. OpenAI integration is optional and is not configured by default.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

### 1. Create and enter a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser. The SQLite database is created automatically on first run.

## Project structure

```text
ai-task-assistant/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Push to a new GitHub repository

Create a new **empty** repository on GitHub named `ai-task-assistant`. Do not initialize it with a README if you plan to push this folder as-is.

Then run these commands from this project folder:

```bash
git init
git add .
git commit -m "Build Taskmate full-stack task manager"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-task-assistant.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Security notes

- Do not commit `.env` files, passwords, tokens, or API keys.
- `tasks.db` is ignored by Git because it is a local development database.
- Flask debug mode is enabled for local development only. Turn it off before deploying publicly.

## Next improvements

- Add OpenAI-powered task breakdowns using a server-side API key
- Add task editing and due dates
- Deploy the app online
