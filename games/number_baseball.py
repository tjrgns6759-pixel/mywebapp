import random
import streamlit as st


def make_answer():
    nums = list(range(10))
    random.shuffle(nums)
    return nums[:4]


def check(answer, guess):
    strike = 0
    ball = 0

    for i in range(4):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    return strike, ball


def run():
    st.header("⚾ 숫자야구")

    st.write("""
    ### 규칙
    - 서로 다른 숫자 4개를 맞추세요.
    - 자리와 숫자가 같으면 **Strike**
    - 숫자만 같으면 **Ball**
    """)

    # 게임 시작
    if "answer" not in st.session_state:
        st.session_state.answer = make_answer()
        st.session_state.history = []
        st.session_state.clear_input = False

    guess = st.text_input(
        "4자리 숫자를 입력하세요",
        key="guess"
    )

    col1, col2 = st.columns(2)

    with col1:
        submit = st.button("확인")

    with col2:
        restart = st.button("새 게임")

    if restart:
        st.session_state.answer = make_answer()
        st.session_state.history = []
        st.rerun()

    if submit:

        if len(guess) != 4:
            st.error("4자리 숫자를 입력하세요.")
            return

        if not guess.isdigit():
            st.error("숫자만 입력하세요.")
            return

        if len(set(guess)) != 4:
            st.error("중복 없는 숫자를 입력하세요.")
            return

        guess_nums = list(map(int, guess))

        strike, ball = check(st.session_state.answer, guess_nums)

        st.session_state.history.append(
            (guess, strike, ball)
        )

        if strike == 4:
            st.success("🎉 정답입니다!")

            st.balloons()

            st.write("정답 :", "".join(map(str, st.session_state.answer)))

    st.divider()

    st.subheader("기록")

    if len(st.session_state.history) == 0:
        st.write("아직 시도한 기록이 없습니다.")

    else:
        for i, (g, s, b) in enumerate(reversed(st.session_state.history), 1):
            st.write(f"{i}. {g} → {s} Strike / {b} Ball")
