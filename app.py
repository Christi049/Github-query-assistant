import streamlit as st
from backend.vector_store import search
from backend.llm_explainer import explain_code

st.set_page_config(page_title="GitHub Repo Assistant", layout="wide")
st.title("🧠 GitHub Repository Intelligent Query System")

# store chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# display old messages
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# input
question = st.chat_input("Ask a question about the repository...")

if question:
    # show user
    st.session_state.messages.append(("user", question))
    with st.chat_message("user"):
        st.markdown(question)

    # retrieve
    with st.spinner("Finding relevant code..."):
        chunks = search(question, k=3)

    # generate answer (YOUR LLM)
    with st.spinner("Generating explanation..."):
        answer = explain_code(question, chunks)

    # show assistant
    st.session_state.messages.append(("assistant", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
