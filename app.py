import streamlit as st
from src.rag_pipeline import process_video, ask_question

# -----------------------
# Session State
# -----------------------
if "video_id" not in st.session_state:
    st.session_state.video_id = None

if "url" not in st.session_state:
    st.session_state.url = ""

if "question" not in st.session_state:
    st.session_state.question = ""

# -----------------------
# Page Title
# -----------------------
st.title("🎥 YouTube RAG Assistant")
st.caption("Ask questions about any YouTube video using AI")

st.divider()

# -----------------------
# URL Section (SAFE STATE)
# -----------------------
url = st.text_input(
    "Enter YouTube URL",
    value=st.session_state.url,
    placeholder="https://www.youtube.com/watch?v=..."
)

st.session_state.url = url

# -----------------------
# Process Button
# -----------------------
if st.button("Process Video", use_container_width=True):

    if not url or not url.strip():
        st.warning("Please enter a YouTube URL.")

    elif "youtube.com" not in url and "youtu.be" not in url:
        st.error("Invalid YouTube URL. Please enter a valid link.")

    elif " " in url or url.lower().startswith("pip"):
        st.error("Invalid input detected. Please enter only a YouTube URL.")

    else:
        with st.spinner("Processing video..."):
            st.session_state.video_id = process_video(url)

        st.success("Video processed successfully!")
        st.write(st.session_state.video_id)

st.divider()

# -----------------------
# Question Section
# -----------------------
col1, col2 = st.columns([5, 1])

with col1:
    question = st.text_input(
        "Ask a Question",
        value=st.session_state.question,
        placeholder="Ask anything about the video..."
    )

    st.session_state.question = question

with col2:
    st.write("")
    st.write("")
    ask_button = st.button("Ask", use_container_width=True)

# -----------------------
# Answer Generation
# -----------------------
if ask_button:

    if not st.session_state.video_id:
        st.warning("Please process a video first.")

    elif not question or not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching video and generating answer..."):

            result = ask_question(
                question,
                st.session_state.video_id
            )

        st.divider()

        st.markdown("### Answer")
        st.markdown(result["answer"])