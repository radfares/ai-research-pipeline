"""GPT-based summarization."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_results(docs, query):
    ctx = "\n\n".join(f"- {d[:800]}" for d in docs[:5])
    prompt = f"""Based on the context below, answer the query in 3-5 sentences.

Query: {query}

Context:
{ctx}
"""
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def daily_digest(docs):
    return summarize_results(docs, "Summarize the latest AI news and launches today.")
