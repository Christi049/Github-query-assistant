import streamlit as st
from backend.repo_loader import clone_repo
from backend.index_repo import index_repository, collection_exists
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

if "repo_url" not in st.session_state:
    st.session_state.repo_url = None

if st.button("Clone and Index"):

    if repo_url:

        if st.session_state.repo_url == repo_url and st.session_state.collection_name:
            st.success("Repository already loaded in this session ✅")
        else:
            with st.spinner("Cloning repository..."):
                repo_path, repo_name = clone_repo(repo_url)

            st.session_state.collection_name = repo_name
            st.session_state.repo_url = repo_url

            if collection_exists(repo_name):
                st.success(f"Repository '{repo_name}' already indexed ✅")
            else:
                with st.spinner("Indexing repository..."):
                    index_repository(repo_path, repo_name)
                st.success(f"Repository '{repo_name}' indexed successfully! 🚀")


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
        
        st.markdown("### Sources")
        for chunk in retrieved_chunks:
            st.code(chunk["file_path"])
    else:
        st.error("Please enter a question.")