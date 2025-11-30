from datetime import datetime, timezone, timedelta


def score_task(task):
    """
    Compute a priority score for a task.

    Input: `task` is a dict-like object with keys: title, due_date (datetime or None),
    importance (int 1-10), effort (hours int/float), created_at (datetime)

    Returns: float priority (higher = should be done sooner).

    Heuristics:
    - Importance (1-10) is the strongest positive factor.
    - Smaller effort increases priority (quick wins) but we scale by importance.
    - Due date approaching increases priority; past-due gives a strong boost.
    - Missing values are handled with sane defaults.
    """
    now = datetime.now(timezone.utc)

    # Handle missing fields with defaults
    importance = task.get('importance')
    if importance is None:
        importance = 5.0
    importance = float(max(1, min(10, importance)))

    effort = task.get('effort')
    if effort is None or effort <= 0:
        # unknown or zero effort -> assume 1 hour to favor quick resolution
        effort = 1.0
    else:
        effort = float(effort)

    due = task.get('due_date')
    if due is None:
        # no due date -> treat as far in the future
        days_until_due = 365.0
    else:
        # normalize to aware datetime
        if due.tzinfo is None:
            due = due.replace(tzinfo=timezone.utc)
        delta = due - now
        days_until_due = delta.total_seconds() / 86400.0

    # Due factor: tasks past due get a large boost; tasks due sooner get higher score
    if days_until_due < 0:
        due_factor = 3.0 + max(0.0, -days_until_due / 7.0)  # overdue adds more weight
    else:
        # inverse relation: closer due => higher factor; cap growth
        due_factor = 1.0 + max(0.0, (30.0 - days_until_due) / 30.0)

    # Effort factor: smaller effort increases priority. Use diminishing returns.
    effort_factor = 1.0 / (1.0 + (effort - 1.0) / 5.0)

    # Compute a base score combining importance and due date, scaled by effort
    score = (importance ** 1.4) * due_factor * effort_factor

    # Small tweak: if created long ago and no due date, slightly increase priority
    created_at = task.get('created_at')
    if created_at:
        age_days = (now - created_at).total_seconds() / 86400.0
        if age_days > 30 and (task.get('due_date') is None):
            score *= 1.1

    # Ensure finite and return
    try:
        if score != score or score == float('inf'):
            score = 0.0
    except Exception:
        score = 0.0

    return float(score)
