def assign_tasks(date_str, users, tasks):
    import copy
    users_copy = copy.deepcopy(users)
    result = []

    for task in sorted(tasks, key=lambda x: -x["points"]):
        available = sorted(
            [u for u in users_copy if date_str not in u["unavailable"]],
            key=lambda x: x["points"]
        )
        if not available:
            result.append({"task": task["name"], "assigned_to": "未割り当て"})
            continue
        assigned = available[0]
        assigned["points"] += task["points"]
        result.append({
            "task": task["name"],
            "assigned_to": assigned["name"],
            "done": False,
            "thanks": 0
        })
    return result, users_copy
