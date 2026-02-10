import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def explain_code(question, retrieved_chunks):

    context = "\n\n".join(
        f"{c['file_path']} lines {c['start_line']}-{c['end_line']}:\n{c['content'][:600]}"
        for c in retrieved_chunks
    )

    prompt = f"""
You are a programming tutor.

Answer using ONLY the provided repository code.

Question:
{question}

Code:
{context}

Give a clear explanation.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]
