import streamlit as st
from datetime import datetime

st.title("曜日判定アプリ")

# テキストボックスで日付を入力（YYYY-MM-DD形式）
date_input = st.text_input("日付を入力（YYYY-MM-DD）", "")

# ボタンを押すと曜日を判定
if st.button("曜日判定"):
    try:
        # 入力された日付を解析
        date_object = datetime.strptime(date_input, "%Y-%m-%d")
        weekday = date_object.strftime("%A")  # 英語の曜日
        weekday_jp = {
            "Monday": "月曜日",
            "Tuesday": "火曜日",
            "Wednesday": "水曜日",
            "Thursday": "木曜日",
            "Friday": "金曜日",
            "Saturday": "土曜日",
            "Sunday": "日曜日",
        }
        st.success(f"その日は {weekday_jp[weekday]} です")
    except ValueError:
        st.error("正しい日付（YYYY-MM-DD）を入力してください。")
