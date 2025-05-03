import streamlit as st
import json
import os
from assigner import assign_tasks
from discord_notify import send_notification

DATA_DIR = "data/"
ASSIGN_FILE = os.path.join(DATA_DIR, "assignments.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

def load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def run():
    st.header("📅 割り当てと完了管理")

    date_str = st.date_input("対象日を選んでね").strftime("%Y-%m-%d")
    users = load_json(USERS_FILE)
    tasks_all = load_json(TASKS_FILE)
    assignments = load_json(ASSIGN_FILE)

    daily_tasks = tasks_all

    if st.button("割り当て開始"):
        result, updated_users = assign_tasks(date_str, users, daily_tasks)
        assignments[date_str] = result
        save_json(ASSIGN_FILE, assignments)
        save_json(USERS_FILE, updated_users)
        st.success("割り当て完了！")

        # 通知送信
        message = f"📅 {date_str} の家事割り当てが完了しました！\n\n"
        for entry in result:
            message += f"🧹 {entry['task']} → 👤 {entry['assigned_to']}\n"
        send_notification(message)

    st.subheader("📋 今日の担当")
    today = assignments.get(date_str, [])
    updated = False

    for entry in today:
        col1, col2, col3 = st.columns(3)
        col1.write(f"🧹 {entry['task']}")
        col2.write(f"👤 {entry['assigned_to']}")

        if not entry.get("done"):
            if col3.button("完了", key=f"{entry['task']}-done"):
                entry["done"] = True
                # ポイント加算
                for user in users:
                    if user["name"] == entry["assigned_to"]:
                        user["points"] += entry["points"]
                        break
                updated = True
        else:
            col3.write("✅ 完了済み")

        if col3.button("👏", key=f"{entry['task']}-thanks"):
            entry["thanks"] = entry.get("thanks", 0) + 1
            updated = True

    if updated:
        save_json(ASSIGN_FILE, assignments)
        save_json(USERS_FILE, users)
