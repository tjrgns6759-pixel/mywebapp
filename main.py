import streamlit as st
from number_baseball import run

st.set_page_config(
    page_title="🎮 미니게임 사이트",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 미니게임 모음")

menu = st.sidebar.selectbox(
    "게임 선택",
    ["숫자야구"]
)

if menu == "숫자야구":
    run()
