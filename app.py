import streamlit as st

from file_reader import (
    read_pdf,
    read_docx,
    read_txt
)

from revision_generator import (
    generate_revision_notes
)

from quiz_generator import (
    generate_quiz
)

from interview_generator import (
    generate_interview_questions
)

from chat_generator import (
    ask_notes_question
)

from pdf_generator import (
    create_pdf
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI STUDY NOTES ASSISTANT | Smart Learning",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# SESSION STATE
# ==================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""

if "revision_notes" not in st.session_state:
    st.session_state.revision_notes = ""

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = ""

# ==================================================
# EXTREMELY BEAUTIFUL CUSTOM CSS
# ==================================================

st.markdown("""
<style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&family=Space+Grotesk:wght@400;500;600&display=swap');

    * {
        font-family: 'Inter', 'Space Grotesk', sans-serif;
    }

    /* Main background with animated gradient */
    .main {
        background: radial-gradient(circle at 20% 30%, rgba(15, 25, 45, 0.05) 0%, rgba(30, 40, 60, 0.02) 100%);
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {background: rgba(255,255,255,0.7); backdrop-filter: blur(12px);}

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #eef2ff;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #3b82f6, #a855f7);
        border-radius: 10px;
    }

    /* Glassmorphic sidebar */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255,255,255,0.5);
        box-shadow: 8px 0 32px rgba(0,0,0,0.05);
    }

    /* Hero section - animated gradient */
    .hero-luxury {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        background-size: 200% 200%;
        animation: gradientShift 8s ease infinite;
        border-radius: 42px;
        padding: 2.5rem 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 25px 40px -12px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    .hero-luxury::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
        opacity: 0.5;
        animation: rotate 20s linear infinite;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .hero-luxury h1 {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;  /* Solid white for maximum visibility */
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    .hero-luxury p {
        color: #e2e8f0;  /* Light gray, much brighter than before */
        font-size: 1.2rem;
        font-weight: 400;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }

    /* Metric cards - 3D effect */
    .metric-glass {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 32px;
        padding: 1.2rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.6);
        box-shadow: 0 8px 20px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.02);
        transition: all 0.35s cubic-bezier(0.2, 0.9, 0.4, 1.1);
    }
    .metric-glass:hover {
        transform: translateY(-6px) scale(1.02);
        background: rgba(255, 255, 255, 0.85);
        box-shadow: 0 20px 30px -12px rgba(0,0,0,0.15);
        border-color: #a78bfa;
    }
    .metric-icon {
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }
    .metric-title {
        font-weight: 700;
        font-size: 1.1rem;
        margin: 0;
        color: #1e293b;
    }
    .metric-desc {
        font-size: 0.8rem;
        color: #475569;
    }

    /* Glowing buttons */
    .stButton > button {
        background: linear-gradient(95deg, #6366f1 0%, #8b5cf6 100%);
        border: none;
        border-radius: 60px;
        padding: 0.65rem 1.8rem;
        font-weight: 600;
        font-size: 0.9rem;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        letter-spacing: 0.01em;
    }
    .stButton > button:hover {
        transform: scale(1.03);
        background: linear-gradient(95deg, #8b5cf6 0%, #6366f1 100%);
        box-shadow: 0 8px 22px rgba(139, 92, 246, 0.4);
        color: white;
    }
    .stButton > button:active {
        transform: scale(0.98);
    }

    /* File uploader */
    div[data-testid="stFileUploader"] {
        background: rgba(255,255,240,0.5);
        border-radius: 40px;
        padding: 0.5rem;
        border: 2px dashed #c7d2fe;
        transition: all 0.2s;
    }
    div[data-testid="stFileUploader"]:hover {
        border-color: #8b5cf6;
        background: rgba(255,255,255,0.8);
    }

    /* Tabs - modern pill design */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(241, 245, 249, 0.7);
        backdrop-filter: blur(4px);
        border-radius: 100px;
        padding: 6px;
        border: 1px solid rgba(255,255,255,0.6);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 40px;
        padding: 8px 24px;
        font-weight: 600;
        color: #334155;
        transition: all 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(120deg, #ffffff, #f8fafc);
        color: #4f46e5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #e0e7ff;
    }

    /* Chat bubbles with gradients */
    .chat-user-premium {
        background: linear-gradient(135deg, #e0e7ff 0%, #ede9fe 100%);
        border-radius: 28px 28px 12px 28px;
        padding: 14px 20px;
        margin: 16px 0;
        border: 1px solid rgba(139, 92, 246, 0.2);
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .chat-ai-premium {
        background: linear-gradient(135deg, #ffffff 0%, #fefce8 100%);
        border-radius: 28px 28px 28px 12px;
        padding: 14px 20px;
        margin: 16px 0;
        border: 1px solid #fde68a;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
    }

    /* Content cards */
    .content-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(8px);
        border-radius: 32px;
        padding: 1.8rem;
        border: 1px solid rgba(255,255,255,0.6);
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05);
        transition: all 0.25s;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(248, 250, 252, 0.8);
        border-radius: 40px;
        font-weight: 600;
        color: #1e293b;
    }

    /* Custom dividers */
    .gradient-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #a78bfa, #60a5fa, transparent);
        margin: 1.5rem 0;
    }

    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 48px;
        border: 1px solid #e2e8f0;
        padding: 0.6rem 1.2rem;
        background: white;
        transition: all 0.2s;
    }
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 0 0 2px rgba(139,92,246,0.2);
    }

    /* Radio buttons (quiz) */
    .stRadio > div {
        gap: 12px;
    }
    .stRadio label {
        background: #f8fafc;
        padding: 0.5rem 1rem;
        border-radius: 60px;
        border: 1px solid #e2e8f0;
        transition: all 0.15s;
    }
    .stRadio label:hover {
        background: #ede9fe;
        border-color: #a78bfa;
    }

    /* Success/info toasts */
    .stAlert {
        border-radius: 24px;
        border-left-width: 6px;
    }

    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #8b5cf6, #3b82f6);
        border-radius: 20px;
    }

    /* Floating animation for metric cards */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    .metric-glass {
        animation: float 4s ease-in-out infinite;
        animation-delay: calc(var(--order) * 0.2s);
    }
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR (with new title)
# ==================================================

with st.sidebar:
    st.markdown("### 📘 **AI STUDY NOTES ASSISTANT**")
    st.markdown("#### *Your Personal AI Tutor*")
    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📂 **Upload Notes**",
        type=["pdf", "docx", "txt"],
        help="PDF, Word, or Text files only"
    )

    st.markdown("---")
    st.markdown("### 🚀 **Superpowers**")
    st.markdown("""
    - 📝 **Smart Revision**  
    - 🎯 **Adaptive Quiz**  
    - 🎤 **Interview Coach**  
    - 💬 **Infinite Chat**  
    """)
    st.markdown("---")
    st.caption("⚡ Instant AI · Private · No data stored")

# ==================================================
# HERO SECTION (with improved visibility)
# ==================================================

st.markdown("""
<div class="hero-luxury">
    <h1>📘 AI STUDY NOTES ASSISTANT</h1>
    <p>Your AI-powered companion to turn notes into knowledge — smarter, faster, better.</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# METRIC CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("📝", "AI Notes", "Smart summaries"),
    ("🎯", "Quiz Master", "10 dynamic Qs"),
    ("🎤", "Interview Prep", "15+ Q&A"),
    ("💬", "Chat Genius", "Unlimited Q&A")
]

for idx, (icon, title, desc) in enumerate(metrics):
    with locals()[f"col{idx+1}"]:
        st.markdown(f"""
        <div class="metric-glass" style="--order: {idx};">
            <div class="metric-icon">{icon}</div>
            <p class="metric-title">{title}</p>
            <p class="metric-desc">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

# ==================================================
# FILE PROCESSING
# ==================================================

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()
    extracted_text = ""

    try:
        if file_type == "pdf":
            extracted_text = read_pdf(uploaded_file)
        elif file_type == "docx":
            extracted_text = read_docx(uploaded_file)
        elif file_type == "txt":
            extracted_text = read_txt(uploaded_file)

        if extracted_text:
            st.session_state.extracted_text = extracted_text
            st.success(f"🎉 **Success!** `{uploaded_file.name}` loaded. Ready to rock.")
            st.balloons()
        else:
            st.warning("⚠️ Empty or unreadable content. Try another file.")
    except Exception as e:
        st.error(f"❌ Oops: {str(e)}")

if st.session_state.extracted_text:
    # Preview with nice expander
    with st.expander("📄 **Preview Extracted Text**", expanded=False):
        st.text_area("Content Preview", st.session_state.extracted_text[:1500] + ("..." if len(st.session_state.extracted_text) > 1500 else ""), height=200, disabled=True, label_visibility="collapsed")

    # TABS
    tab1, tab2, tab3, tab4 = st.tabs(["📝 **Revision Notes**", "🎯 **Smart Quiz**", "🎤 **Interview Prep**", "💬 **AI Chat**"])

    # ========== TAB 1: REVISION NOTES ==========
    with tab1:
        col_gen, col_dl = st.columns([3, 1])
        with col_gen:
            if st.button("✨ **Generate Revision Notes**", use_container_width=True):
                with st.spinner("🧠 Synthesizing knowledge..."):
                    st.session_state.revision_notes = generate_revision_notes(st.session_state.extracted_text)
                st.toast("✅ Notes created!", icon="🎉")

        if st.session_state.revision_notes:
            st.markdown("---")
            st.markdown("#### 📖 **Your AI-Generated Notes**")
            with st.container():
                st.markdown(f"<div class='content-card'>{st.session_state.revision_notes}</div>", unsafe_allow_html=True)
            pdf_data = create_pdf("Revision Notes", st.session_state.revision_notes)
            with col_dl:
                st.download_button("📥 **Download PDF**", pdf_data, file_name="Revision_Notes.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.info("👆 Click above to transform your notes into structured revision material.")

    # ========== TAB 2: QUIZ ==========
    with tab2:
        if st.button("🎲 **Generate Quiz**", use_container_width=False):
            with st.spinner("Designing quiz questions..."):
                st.session_state.quiz_data = generate_quiz(st.session_state.extracted_text)
            st.toast("Quiz ready! Challenge yourself.", icon="🏆")

        if st.session_state.quiz_data:
            st.markdown("---")
            st.markdown("#### 📋 **Quiz Time**")
            answers = []
            for idx, q in enumerate(st.session_state.quiz_data):
                st.markdown(f"**Q{idx+1}. {q['question']}**")
                selected = st.radio("", q["options"], key=f"q_{idx}", label_visibility="collapsed")
                answers.append(selected)
                st.markdown("<hr style='margin: 0.5rem 0; opacity:0.3;'>", unsafe_allow_html=True)

            if st.button("✅ **Submit Answers**", type="primary"):
                score = sum(1 for i, a in enumerate(answers) if a == st.session_state.quiz_data[i]["answer"])
                total = len(st.session_state.quiz_data)
                perc = (score / total) * 100
                st.progress(int(perc))
                st.success(f"🎯 **Score: {score}/{total}**")
                st.info(f"📊 **Accuracy: {perc:.1f}%**")
                with st.expander("🔍 **Review answers**"):
                    for i, q in enumerate(st.session_state.quiz_data):
                        correct = q["answer"]
                        yours = answers[i]
                        if yours == correct:
                            st.markdown(f"✅ **{q['question']}**  →  *{correct}*")
                        else:
                            st.markdown(f"❌ **{q['question']}**  \nYour answer: {yours}  \nCorrect: {correct}")
                        st.markdown("---")
        else:
            st.info("🎯 Click 'Generate Quiz' to start a knowledge check.")

    # ========== TAB 3: INTERVIEW ==========
    with tab3:
        col_int_gen, col_int_dl = st.columns([3, 1])
        with col_int_gen:
            if st.button("🎤 **Generate Interview Qs**", use_container_width=True):
                with st.spinner("Crafting interview Q&As..."):
                    st.session_state.interview_questions = generate_interview_questions(st.session_state.extracted_text)
                st.toast("Interview questions ready!", icon="🎤")

        if st.session_state.interview_questions:
            st.markdown("---")
            st.markdown("#### 🎙️ **Interview Prep Bank**")
            st.markdown(f"<div class='content-card'>{st.session_state.interview_questions}</div>", unsafe_allow_html=True)
            pdf_int = create_pdf("Interview Questions", st.session_state.interview_questions)
            with col_int_dl:
                st.download_button("📥 **Download PDF**", pdf_int, file_name="Interview_Questions.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.info("💡 Hit the button above to generate real-world interview questions from your material.")

    # ========== TAB 4: CHAT ==========
    with tab4:
        st.markdown("#### 💬 **Chat with your notes**")
        col_q, col_clear = st.columns([5, 1])
        with col_q:
            user_q = st.text_input("Ask anything:", placeholder="e.g., Summarize the key takeaways", label_visibility="collapsed")
        with col_clear:
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()

        if st.button("🚀 **Ask AI**", type="primary", use_container_width=False):
            if user_q.strip():
                with st.spinner("🤖 Thinking..."):
                    answer = ask_notes_question(st.session_state.extracted_text, user_q)
                st.session_state.chat_history.append((user_q, answer))
            else:
                st.warning("Please type a question.")

        if st.session_state.chat_history:
            st.markdown("---")
            for q, a in reversed(st.session_state.chat_history):
                st.markdown(f"<div class='chat-user-premium'><strong>🧑 You</strong><br>{q}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='chat-ai-premium'><strong>🤖 AI Tutor</strong><br>{a}</div>", unsafe_allow_html=True)
        else:
            st.caption("✨ Ask a question about your uploaded document. The AI will answer based only on the content.")

else:
    # Beautiful onboarding state
    st.markdown("""
    <div style="background: linear-gradient(145deg, #fef9e3, #fff7ed); border-radius: 48px; padding: 2.5rem; text-align: center; margin-top: 2rem; border: 1px solid #ffedd5;">
        <h3 style="color: #b45309;">🌟 Ready to supercharge your learning with AI STUDY NOTES ASSISTANT?</h3>
        <p style="font-size: 1.1rem;">Upload your notes from the sidebar and let AI do the magic.</p>
        <p style="margin-top: 1rem;">✨ Smart Notes · 🎯 Custom Quiz · 🎤 Interview Qs · 💬 AI Chat</p>
    </div>
    """, unsafe_allow_html=True)