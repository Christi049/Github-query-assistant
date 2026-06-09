# GitHub Query Assistant

GitHub Query Assistant is an AI-powered repository analysis system that enables users to query GitHub repositories using natural language. The system processes source code repositories, generates semantic embeddings for code chunks, stores them in a vector database, and retrieves relevant context to generate accurate explanations using Large Language Models (LLMs).

---

## Features

- Natural language querying of GitHub repositories
- Semantic code search using vector embeddings
- Retrieval-Augmented Generation (RAG) pipeline
- Repository indexing and chunk-based processing
- Context-aware code explanations
- Qdrant vector database integration
- Streamlit-based interactive interface
- Optimized batch embedding and vector storage
- Supports multiple programming languages

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI / NLP
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Mistral API

### Vector Database
- Qdrant Cloud

### Libraries Used
- qdrant-client
- transformers
- sentence-transformers
- requests
- python-dotenv
- GitPython

---

## Project Structure

```bash
Github-query-assistant/
│
├── backend/
│   ├── __init__.py
│   ├── code_parser.py
│   ├── code_reader.py
│   ├── embeddings.py
│   ├── index_repo.py
│   ├── llm_explainer.py
│   ├── repo_loader.py
│   ├── vector_store.py
│   │
│   ├── test_chunk.py
│   ├── test_rag.py
│   ├── test_read.py
│   └── test_vector.py
│
├── .devcontainer/
├── .vscode/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_clone.py
```

---

## System Workflow

1. User provides a GitHub repository URL
2. Repository is cloned temporarily
3. Supported source code files are extracted
4. Files are divided into smaller semantic chunks
5. Embeddings are generated using Sentence Transformers
6. Embeddings and metadata are stored in Qdrant
7. User query is embedded
8. Relevant code chunks are retrieved using vector similarity search
9. Retrieved context is passed to the LLM
10. Final explanation is generated and displayed

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Christi049/Github-query-assistant.git
cd Github-query-assistant
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Environment

##### Windows

```bash
venv\Scripts\activate
```

##### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

## Running the Project

```bash
streamlit run app.py
```

---

## Supported File Types

The system currently supports:

- `.py`
- `.js`
- `.jsx`
- `.ts`
- `.tsx`
- `.java`
- `.cpp`
- `.c`
- `.html`
- `.css`

---

## Optimization Techniques

- Batch embedding generation
- Batch vector uploads to Qdrant
- File-path-aware embeddings
- Chunk-level semantic retrieval
- Collection existence checks before indexing
- Optimized retrieval for large repositories

---

## Example Queries

- How is authentication handled?
- Explain the Redux flow in this project
- Where is API communication implemented?
- Explain the middleware logic
- How are routes managed?

---

## Deployment

The application is deployed using Streamlit Cloud.

---

## Future Enhancements

- Conversational memory
- AST-based code analysis
- Hybrid retrieval methods
- Support for private repositories
- Repository summarization

