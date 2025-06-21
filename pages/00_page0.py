import streamlit as st

# -------------------- 설정 --------------------
st.set_page_config(page_title="마음 건강 자가 진단", layout="centered")
st.title("🧠 마음이 힘든 친구들을 위한 자가 진단 & 셀프케어")

# -------------------- 질문 설정 --------------------
questions = [
    ("요즘 슬프거나 우울한 기분이 자주 든다", "우울증"),
    ("아무것도 하기 싫고 의욕이 없다", "우울증"),
    ("자주 피곤하고 쉽게 지친다", "우울증"),
    ("내가 가치 없다고 느껴질 때가 있다", "우울증"),
    ("불안하거나 긴장된 상태가 계속된다", "불안장애"),
    ("별일 아닌데도 자꾸 걱정이 많아진다", "불안장애"),
    ("사람들과 있을 때 긴장되고 불편하다", "사회불안장애"),
    ("집중이 잘 안 되고 산만하다", "주의력결핍장애"),
    ("충동적으로 말하거나 행동할 때가 많다", "주의력결핍장애"),
    ("식욕이 급격하게 줄거나 늘었다", "섭식장애"),
    ("과식 후 죄책감을 느끼거나 몰래 먹는다", "섭식장애"),
    ("밤에 잠들기 어렵거나 자주 깬다", "우울증"),
    ("과거의 힘든 기억이 자꾸 떠오른다", "외상후스트레스장애"),
    ("예민하고 작은 일에도 쉽게 놀란다", "외상후스트레스장애"),
    ("가끔 모든 것을 끝내고 싶다는 생각이 든다", "우울증"),
    ("몸이 아픈 것도 아닌데 자주 불편하다", "불안장애"),
    ("감정을 조절하기 어려울 때가 있다", "우울증"),
    ("혼자 있고 싶고 사람들을 피하게 된다", "우울증"),
    ("생각이 많아 잠을 못 이루는 날이 많다", "불안장애"),
    ("가끔 현실감이 없고 멍한 상태가 된다", "외상후스트레스장애"),
]

# -------------------- 척도 --------------------
scale = {
    "😐 전혀 그렇지 않다": 0,
    "🙂 가끔 그렇다": 1,
    "😟 자주 그렇다": 2,
}

# -------------------- 상태 초기화 --------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}

# -------------------- 질문 표시 --------------------
if st.session_state.current_q < len(questions):
    q_text, category = questions[st.session_state.current_q]
    st.subheader(f"질문 {st.session_state.current_q + 1}/{len(questions)}")
    response = st.radio(q_text, list(scale.keys()), key=f"q{st.session_state.current_q}")

    if st.button("다음"):
        score = scale[response]
        if category not in st.session_state.scores:
            st.session_state.scores[category] = 0
        st.session_state.scores[category] += score
        st.session_state.current_q += 1
        st.rerun()

# -------------------- 결과 출력 --------------------
else:
    st.header("📝 진단 결과")
    sorted_results = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    main_issue = sorted_results[0][0]
    st.subheader(f"가장 두드러진 경향: **{main_issue}**")

    # -------------------- 셀프케어 제안 --------------------
    st.markdown("### 🏡병원 가기가 두렵다면 우선 집에서 셀프케어를 해보는 건 어때? ")

    tips = {
        "우울증": [
            "가벼운 산책이나 햇볕 쬐기",
            "작은 성취 경험 쌓기 (예: 책 10쪽 읽기)",
            "믿을 수 있는 사람에게 감정 나누기",
        ],
        "불안장애": [
            "심호흡, 명상 등으로 마음 진정시키기",
            "카페인 줄이고 뉴스 과다 섭취 피하기",
            "불안을 글로 써보며 정리하기",
        ],
        "사회불안장애": [
            "간단한 인사부터 연습해보기",
            "안정감을 주는 장소에서 소통 연습",
            "자기 비난보다 자기 수용 연습하기",
        ],
        "주의력결핍장애": [
            "일과를 시각적으로 정리하기 (메모 등)",
            "집중 시간 짧게 설정 + 보상 주기",
            "휴대폰, 알림 등 자극 줄이기",
        ],
        "섭식장애": [
            "정해진 시간에 균형 잡힌 식사하기",
            "자기 몸에 대해 긍정적 사고 연습",
            "혼자보다 함께 식사하기",
        ],
        "외상후스트레스장애": [
            "편안한 환경 조성 & 충분한 휴식",
            "감정을 일기나 그림 등으로 표현하기",
            "자기비난 대신 자기이해 연습하기",
        ],
    }

    for tip in tips.get(main_issue, []):
        st.write(f"- {tip}")

    st.markdown("---")
    st.info("이 결과는 전문 진단이 아닙니다. 증상이 지속되거나 심하다면 꼭 전문가의 도움을 받아보세요.")


# ------------------ 페이지 전환 초기화 ------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# ------------------ 페이지 1: 결과 화면 ------------------
if st.session_state.page == "main":
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔁 다시 시작하기"):
            st.session_state.current_q = 0
            st.session_state.scores = {}
            st.session_state.page = "main"
            st.rerun()

    with col2:
        if st.button("💬 혹시 나랑 더 얘기하고 싶어?"):
            st.session_state.page = "chat"
            st.rerun()

# ------------------ 페이지 2: ChatGPT 상담 ------------------
elif st.session_state.page == "chat":
    st.markdown("## 🤖 ChatGPT와 감정 나누기")
    st.write("지금 어떤 기분이든 괜찮아요. 마음을 편하게 표현해봐요.")

    user_input = st.text_input("💬 당신의 이야기", key="chat_input")

    # 공감 응답 생성 함수 (단순 예시 기반)
    def generate_empathy_response(message):
        keywords = {
            "힘들": "많이 힘드셨죠. 그런 감정을 느끼는 건 너무나 자연스러운 일이에요.",
            "외롭": "외로움을 느낄 때도 있죠. 혼자가 아니라는 걸 잊지 마세요.",
            "불안": "불안한 마음, 참 지치죠. 잠시 숨을 고르고 천천히 이야기해도 괜찮아요.",
            "우울": "우울한 감정은 누구나 겪을 수 있어요. 함께 있어줄게요.",
            "짜증": "짜증날 만한 일이었겠네요. 그렇게 느끼는 건 당연해요.",
            "무기력": "무기력할 땐 아무것도 하기 싫죠. 그냥 가만히 있어도 괜찮아요.",
            "괴로": "그만큼 마음이 아팠던 거겠죠. 그 감정, 소중해요.",
        }
        for word, resp in keywords.items():
            if word in message:
                return resp
        return "이야기해줘서 고마워요. 당신의 감정은 소중하고 존중받아야 해요."

    if user_input:
        bot_response = generate_empathy_response(user_input)

        # 사용자 말풍선
        st.markdown(f"""
        <div style="text-align: right; background-color:#DCF8C6; padding:10px; border-radius:10px; margin:5px; display:inline-block; max-width:75%;">
            <strong>나</strong>: {user_input}
        </div>
        """, unsafe_allow_html=True)

        # 챗지피티 응답 말풍선
        st.markdown(f"""
        <div style="text-align: left; background-color:#F1F0F0; padding:10px; border-radius:10px; margin:5px; display:inline-block; max-width:75%;">
            <strong>ChatGPT</strong>: {bot_response}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔙 결과 페이지로 돌아가기"):
        st.session_state.page = "main"
        st.rerun()
