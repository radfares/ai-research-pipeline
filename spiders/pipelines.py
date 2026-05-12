# pipelines.py — process scraped data: clean, dedupe, embed, store
import os
import json
import hashlib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class CleanAndStorePipeline:
    def __init__(self):
        self.seen = set()
        try:
            from storage.chroma_store import ChromaStore
            self.store = ChromaStore()
        except Exception:
            self.store = None

    def process_item(self, item, spider):
        text = item.get("cleaned_text") or item.get("description") or item.get("abstract") or ""
        if not text:
            return item

        url = item.get("url", "")
        item_id = hashlib.sha256((url + text[:200]).encode()).hexdigest()[:16]
        if item_id in self.seen:
            spider.logger.info(f"Duplicate dropped: {url}")
            return None
        self.seen.add(item_id)

        entry = {
            "id": item_id,
            "title": item.get("title", ""),
            "url": url,
            "source": item.get("source", ""),
            "text": text,
            "tags": item.get("tags", []),
            "scraped_at": datetime.utcnow().isoformat(),
            "type": getattr(spider, "item_type", "article"),
        }

        with open("data/raw.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")

        if self.store and text:
            try:
                self.store.add(
                    ids=[item_id],
                    documents=[text],
                    metadatas=[{
                        "title": entry["title"],
                        "url": entry["url"],
                        "source": entry["source"],
                        "type": entry["type"],
                    }]
                )
            except Exception as e:
                spider.logger.error(f"Chroma store error: {e}")

        return item
