import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def explain_code(question, retrieved_chunks):

    if not retrieved_chunks:
        return "No relevant code found in the repository."

    # Build strict context
    context = "\n\n".join(
        f"""
File: {c['file_path']}
Lines: {c['start_line']}-{c['end_line']}

{c['content'][:800]}
"""
        for c in retrieved_chunks
    )

    prompt = f"""
You are a strict code analysis assistant.

IMPORTANT RULES:
- Use ONLY the provided repository context.
- Do NOT add external knowledge.
- Do NOT explain general concepts unless directly visible in the code.
- If the answer is not present in the context, reply:
  "This information is not present in the repository."
- Keep the answer concise.
- Maximum 5 bullet points.
- No introduction.
- No conclusion.
- Do NOT guess line numbers.

Repository Context:
{context}

Question:
{question}

Answer (bullet points only):
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2  # lower = less rambling
            },
            timeout=120
        )

        data = response.json()

        if "choices" not in data:
            return f"Error from LLM: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error contacting LLM: {str(e)}"