"""CLI to query the knowledge base."""
import sys
from storage.chroma_store import ChromaStore
from summarization.summarizer import summarize_results

def main():
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Latest AI launches this week"
    db = ChromaStore()
    res = db.query(q, n_results=10)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    for i, doc in enumerate(docs):
        m = metas[i]
        print(f"\n[{i+1}] {m['title']}")
        print(f"  URL: {m['url']}")
        print(f"  {doc[:300]}...")
    print("\n--- Summary ---")
    print(summarize_results([docs[i] for i in range(len(docs))], q))

if __name__ == "__main__":
    main()
