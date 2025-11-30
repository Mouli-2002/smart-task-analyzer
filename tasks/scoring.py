from datetime import date

def score_task(task):
    """
    task = {
        "title": "...",
        "due_date": "2025-12-01",
        "estimated_hours": 5,
        "importance": 7,
        "dependencies": ["Task A", "Task B"]
    }
    """
    today = date.today()

    # --- Urgency ---
    due = task.get("due_date")
    if due:
        due = date.fromisoformat(due)
        days_left = (due - today).days
        urgency = 1 / (1 + max(days_left, 0))  # closer deadline => bigger
    else:
        urgency = 0.1  # neutral

    # --- Importance ---
    importance = task.get("importance", 5)
    importance_score = importance / 10   # normalize 1–10 to 0–1

    # --- Effort ---
    hours = max(task.get("estimated_hours", 1), 1)
    effort_score = 1 / (hours + 1)

    # --- Dependency penalty ---
    deps = task.get("dependencies", [])
    dep_penalty = 0.15 * len(deps)  # each dependency reduces score slightly

    # --- Final Score ---
    score = (0.5 * urgency) + (0.3 * importance_score) + (0.2 * effort_score)
    score = score - dep_penalty
    return round(score, 4)
