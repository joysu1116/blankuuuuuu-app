import random
import streamlit as st


def init_state():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "num_uncolored" not in st.session_state:
        st.session_state.num_uncolored = None
    if "num_colored" not in st.session_state:
        st.session_state.num_colored = None
    if "last_problem" not in st.session_state:
        st.session_state.last_problem = None
    if "correct" not in st.session_state:
        st.session_state.correct = False
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""


def generate_new_problem():
    # Ensure new problem differs from last_problem
    last = st.session_state.get("last_problem")
    attempts = 0
    while True:
        num_uncolored = random.randint(5, 20)
        num_colored = random.randint(1, 10)
        total = num_uncolored + num_colored
        problem = (num_colored, total)
        attempts += 1
        # Try until problem is different or we tried a few times
        if problem != last or attempts > 10:
            break

    st.session_state.num_uncolored = num_uncolored
    st.session_state.num_colored = num_colored
    st.session_state.last_problem = problem
    st.session_state.correct = False
    st.session_state.feedback = ""


def reset_quiz():
    st.session_state.started = False
    st.session_state.num_uncolored = None
    st.session_state.num_colored = None
    st.session_state.last_problem = None
    st.session_state.correct = False
    st.session_state.feedback = ""


def show_stars_row(num_colored, num_uncolored):
    # Build a visual group of stars using emojis about 10 per row
    total = num_colored + num_uncolored
    stars = []
    # Mix colored and uncolored so children can count visually — but keep simple patterns
    # We'll place colored then uncolored so it's easy to count the colored ones quickly
    stars.extend(["🌟"] * num_colored)
    stars.extend(["⭐"] * num_uncolored)

    # Split into rows of max 10 per row
    rows = ["".join(stars[i : i + 10]) for i in range(0, len(stars), 10)]
    for row in rows:
        st.markdown(f"<div style='font-size:42px; line-height:1.1'>{row}</div>", unsafe_allow_html=True)


def parse_fraction_input(text: str):
    """Parses inputs like 'a/b'. Returns (a, b) or (None, None) on invalid."""
    try:
        text = text.strip()
        if "/" not in text:
            return None, None
        a_str, b_str = text.split("/", 1)
        a = int(a_str.strip())
        b = int(b_str.strip())
        return a, b
    except Exception:
        return None, None


def main():
    init_state()

    st.set_page_config(page_title="분수 별 놀이", page_icon="🌟", layout="centered")
    st.title("🌟 분수로 배우는 스타 게임 (3학년)")

    st.markdown("""
    ### 학습 목표
    - 빛나는 별의 개수를 전체 별의 수로 나타내는 '분수'를 연습해요.
    - 예: 빛나는 별 3개, 전체 8개 → 분수는 3/8
    """)

    # Start and reset buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if not st.session_state.started:
            if st.button("시작하기 🎉"):
                st.session_state.started = True
                generate_new_problem()
    with col2:
        if st.button("새 문제 / 초기화 🔁"):
            reset_quiz()

    # If not started, show friendly prompt
    if not st.session_state.started:
        st.info("시작 버튼을 눌러 문제를 만들어보세요. 아주 쉬운 레이아웃이에요 — 빛나는 별(🌟)을 세어 보세요!")
        st.stop()

    # Now we have a problem
    num_uncolored = st.session_state.num_uncolored
    num_colored = st.session_state.num_colored
    total = num_colored + num_uncolored

    st.subheader("문제를 잘 읽고 분수를 입력해보세요 ✍️")
    st.markdown("(a/b 형태로 입력 — a는 빛나는 별의 개수, b는 전체 별의 개수)  ")

    # show the stars
    show_stars_row(num_colored, num_uncolored)

    # Problem hint removed (per request) — no teacher hint shown to students

    # Input area
    with st.form(key="answer_form"):
        answer = st.text_input("분수를 입력해보세요 (예: 3/8)")
        submitted = st.form_submit_button("제출하기 ✅")

    if submitted:
        a, b = parse_fraction_input(answer)
        if a is None or b is None:
            st.warning("입력 형식이 잘못되었어요. 'a/b' 형태로 숫자를 입력해 주세요. 예: 3/8")
        else:
            # Accept exact match or equivalent fraction after simplifying
            from math import gcd

            def simplify(x, y):
                if y == 0:
                    return None, None
                g = gcd(x, y)
                return x // g, y // g

            # Expected fraction (num_colored / total)
            exp_num, exp_den = simplify(num_colored, total)
            user_num, user_den = simplify(a, b)

            if (a == num_colored and b == total) or (user_num == exp_num and user_den == exp_den):
                st.session_state.correct = True
                st.success("정답이에요! 멋져요 🎉 다음 문제로 넘어갑니다.")
                # generate a brand new problem (different numbers)
                generate_new_problem()
                # Immediately rerun so the new problem shows right away
                # `st.experimental_rerun` was removed in some Streamlit versions; use `st.rerun()` instead
                st.rerun()
            else:
                st.session_state.correct = False
                st.error("틀렸어요! 다시 시도해보세요.")
                # keep same problem — do not generate


if __name__ == "__main__":
    main()
