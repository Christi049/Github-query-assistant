from backend.vector_store import search
from backend.llm_explainer import explain_code

question = input("Ask a question:\n> ")

retrieved = search(question, k=3)

print("\nGenerating explanation...\n")
answer = explain_code(question, retrieved)

print(answer)
