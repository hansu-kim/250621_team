import streamlit as st
import random

st.set_page_config(page_title="상담 챗봇 도우미", page_icon="💬")
st.title("💬 ChatGPT 상담 도우미")

# 상담 주제별 질문 리스트
topics = {
    "🎯 진로 고민": [
        "저는 적성에 맞는 직업을 찾고 싶습니다.",
        "대학 전공 선택에 고민이 많습니다.",
        "앞으로 유망한 직업이나 산업이 궁금합니다."
    ],
    "🧠 성격 분석": [
        "제 성격의 강점과 단점을 알고 싶어요.",
        "어떤 상황에서 성격이 장점/단점이 될 수 있을지 궁금합니다.",
        "사람들과 잘 어울리는 법에 대해 조언을 듣고 싶어요."
    ],
    "📚 학습 습관": [
        "효율적인 공부 루틴을 만들고 싶어요.",
        "집중력이 부족할 때 어떻게 해야 할까요?",
        "시험 전 정리와 복습 방법이 궁금합니다."
    ],
    "🤝 친구 관계": [
        "친구와 오해가 생겼을 때 어떻게 화해할 수 있을까요?",
        "새로운 친구를 사귀는 방법이 궁금해요.",
        "친구들과 어울릴 때 너무 소극적인 제 성격이 고민입니다."
    ],
    "🏠 가족 문제": [
        "부모님과 자주 갈등이 생겨요.",
        "가족의 기대가 부담스러워요.",
        "형제자매와 자주 다툽니다. 화목해지고 싶어요."
    ],
    "❤️ 연애 고민": [
        "좋아하는 사람에게 다가가는 방법이 궁금합니다.",
        "짝사랑 중인데 마음을 표현해야 할지 고민이에요.",
        "연애 중 자주 싸우게 되는데, 건강한 관계를 유지하고 싶어요."
    ],
    "🧘 스트레스 해소": [
        "스트레스를 효과적으로 푸는 방법을 알고 싶어요.",
        "공부나 일에 지쳤을 때 다시 동기부여를 얻고 싶습니다.",
        "불안하거나 예민할 때 마음을 진정시키는 법을 알고 싶어요."
    ]
}

# 주제 선택
selected_topic = st.selectbox("📌 상담 주제를 선택하세요", list(topics.keys()))
questions = topics[selected_topic]

# 랜덤 질문 2~3개 선택해서 줄바꿈 포함한 프롬프트 조합
sampled_questions = random.sample(questions, min(3, len(questions)))
combined_prompt = "안녕하세요. 다음과 같은 고민이 있습니다:\n" + "\n".join(f"- {q}" for q in sampled_questions) + "\n조언 부탁드립니다."

# 추천 질문 표시
st.subheader("✍️ 추천 질문:")
for i, q in enumerate(questions, 1):
    st.markdown(f"**{i}.** {q}")

# 생성된 문장 표시
st.subheader("🧩 자동 생성 프롬프트")
st.text_area("복사할 내용", combined_prompt, height=150)

# 복사 버튼 + 메시지 출력
copy_code = f"""
<script>
function copyPrompt() {{
    navigator.clipboard.writeText(`{combined_prompt}`).then(function() {{
        const status = document.getElementById("copy-status");
        status.innerText = "✅ 복사 완료!";
        status.style.color = "green";
    }});
}}
</script>
<button onclick="copyPrompt()" style="
    background-color:#4CAF50;
    color:white;
    padding:10px 20px;
    border:none;
    border-radius:5px;
    cursor:pointer;
    font-size:16px;
">📋 프롬프트 복사하기</button>
<p id="copy-status" style="margin-top:10px;font-weight:bold;"></p>
"""

st.markdown(copy_code, unsafe_allow_html=True)

# 챗봇 링크
st.subheader("🌐 챗봇 상담 링크")
st.markdown("""
- 🤖 [ChatGPT (OpenAI)](https://chat.openai.com)
- 🌟 [Gemini (Google)](https://gemini.google.com/)
- 💬 [Claude (Anthropic)](https://claude.ai/)
- 🧠 [Hugging Face Chat](https://huggingface.co/chat)

위 프롬프트를 복사하여 원하는 챗봇에 붙여 넣고 상담을 시작해 보세요.
""")
