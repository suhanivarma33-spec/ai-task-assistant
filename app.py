from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "tasks.db"


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                details TEXT DEFAULT '',
                priority TEXT NOT NULL DEFAULT 'Medium',
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def index():
    with get_db() as db:
        tasks = db.execute("SELECT * FROM tasks ORDER BY completed ASC, id DESC").fetchall()
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    return render_template("index.html", tasks=tasks, total=total, completed=completed)


@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()
    details = request.form.get("details", "").strip()
    priority = request.form.get("priority", "Medium")
    if priority not in {"Low", "Medium", "High"}:
        priority = "Medium"
    if title:
        with get_db() as db:
            db.execute(
                "INSERT INTO tasks (title, details, priority) VALUES (?, ?, ?)",
                (title[:120], details[:500], priority),
            )
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/toggle")
def toggle_task(task_id):
    with get_db() as db:
        db.execute(
            "UPDATE tasks SET completed = CASE WHEN completed = 0 THEN 1 ELSE 0 END WHERE id = ?",
            (task_id,),
        )
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    with get_db() as db:
        db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for("index"))


@app.post("/api/suggestion")
def suggestion():
    """A no-key local helper. Replace with an OpenAI API call when ready."""
    data = request.get_json(silent=True) or {}
    task = str(data.get("task", "")).strip()
    if not task:
        return jsonify({"suggestion": "Enter a task first."}), 400
    suggestion_text = (
        f"Start by defining the finish line for “{task[:160]}”. "
        "Break it into 3 small steps: prepare what you need, complete the main action, "
        "then review the result. Do the first step in a focused 15-minute session."
    )
    return jsonify({"suggestion": suggestion_text})


init_db()

if __name__ == "__main__":
    app.run(debug=True)
