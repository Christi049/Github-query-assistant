import streamlit as st
from backend.repo_loader import clone_repo
from backend.index_repo import index_repository
from backend.vector_store import search
from backend.llm_explainer import explain_code

st.title("GitHub Query Assistant")

# -----------------------
# Session State
# -----------------------

if "collection_name" not in st.session_state:
    st.session_state.collection_name = None


# -----------------------
# Repository Input
# -----------------------

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Clone and Index"):

    if repo_url:
        with st.spinner("Cloning repository..."):
            repo_path, repo_name = clone_repo(repo_url)

        with st.spinner("Indexing repository..."):
            index_repository(repo_path, repo_name)

        # Save collection name in session
        st.session_state.collection_name = repo_name

        st.success(f"Repository '{repo_name}' indexed successfully!")
    else:
        st.error("Please enter a valid repository URL.")


# -----------------------
# Question Section
# -----------------------

question = st.text_input("Ask a question about the repository")

if st.button("Ask Question"):

    if not st.session_state.collection_name:
        st.error("Please index a repository first.")
    elif question:
        with st.spinner("Retrieving relevant code..."):
            retrieved_chunks = search(
                question,
                st.session_state.collection_name
            )

        with st.spinner("Generating answer..."):
            answer = explain_code(question, retrieved_chunks)

        st.markdown("### Answer")
        st.write(answer)
    else:
        st.error("Please enter a question.")