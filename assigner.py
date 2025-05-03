# assigner.py

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
            result.append({
                "task": task["name"],
                "assigned_to": "未割り当て",
                "done": False,
                "thanks": 0,
                "points": task["points"]
            })
            continue

        assigned = available[0]
        result.append({
            "task": task["name"],
            "assigned_to": assigned["name"],
            "done": False,
            "thanks": 0,
            "points": task["points"]
        })

    return result, users_copy
