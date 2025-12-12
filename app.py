import streamlit as st
import os

st.set_page_config(page_title="장애물 피하기 게임", layout="wide")

st.title("🎮 장애물 피하기 게임 (Streamlit + HTML 통합)")

st.write("""
스페이스바 또는 화면 클릭으로 점프하세요!  
아래에 게임 화면이 로드됩니다.
""")

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "game", "index.html")

with open(html_path, 'r', encoding='utf-8') as f:
    html_data = f.read()

st.components.v1.html(html_data, height=430, scrolling=False)
