import streamlit as st
import task_input
import user_input
import assign_view

st.set_page_config(page_title="FairTask", layout="centered")
st.title("FairTask")

page = st.sidebar.selectbox("ページを選んでね", ["家事タスク登録", "メンバー登録", "割り当て＆完了"])

if page == "家事タスク登録":
    task_input.run()
elif page == "メンバー登録":
    user_input.run()
elif page == "割り当て＆完了":
    assign_view.run()
