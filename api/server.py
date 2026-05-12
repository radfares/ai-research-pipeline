"""FastAPI server for remote queries."""
from fastapi import FastAPI
from storage.chroma_store import ChromaStore
from summarization.summarizer import summarize_results

app = FastAPI(title="AI Research Pipeline API")
db = ChromaStore()

@app.get("/query")
def query(q: str, n: int = 5):
    res = db.query(q, n_results=n)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    return {
        "query": q,
        "results": [{
            "title": m["title"],
            "url": m["url"],
            "text": d[:500]
        } for m, d in zip(metas, docs)],
        "summary": summarize_results(docs, q)
    }
