import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scoring import score_task


@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    data = json.loads(request.body.decode("utf-8"))
    tasks = data.get("tasks", [])

    # Score each task
    for task in tasks:
        task["score"] = score_task(task)

    # Sort by score (high → low)
    tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)

    return JsonResponse({"tasks": tasks}, safe=False)


@csrf_exempt
def suggest_tasks(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET required"}, status=400)

    # Example: Accept tasks through query or static testing
    # For now, just respond with simple template:
    suggestions = [
        "Work on urgent & important tasks first",
        "Avoid tasks with too many dependencies",
        "Prefer short tasks when your time is limited"
    ]

    return JsonResponse({
        "top_3": suggestions[:3],
        "message": "Focus on tasks that combine high importance and high urgency with low effort."
    })
