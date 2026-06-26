import streamlit as st
from src.rag_pipeline import process_video, ask_question

# Session State
if "video_id" not in st.session_state:
    st.session_state.video_id = None

# Page Title
st.title("🎥 YouTube RAG Assistant")
st.caption("Ask questions about any YouTube video using AI")

st.divider()

# URL Section
url = st.text_input(
    "Enter YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("Process Video", use_container_width=True):

    if not url.strip():
        st.warning("Please enter a YouTube URL.")

    else:
        with st.spinner("Processing video..."):

            st.session_state.video_id = process_video(url)

        st.success("Video processed successfully!")
        st.write(st.session_state.video_id)

st.divider()

# Question Section
col1, col2 = st.columns([5, 1])

with col1:
    question = st.text_input(
        "Ask a Question",
        placeholder="Ask anything about the video..."
    )

with col2:
    st.write("")
    st.write("")
    ask_button = st.button(
        "Ask",
        use_container_width=True
    )

# Answer Generation
if ask_button:

    if not st.session_state.video_id:
        st.warning("Please process a video first.")

    elif not question.strip():
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