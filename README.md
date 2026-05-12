# AI Research Pipeline

An automated intelligence system for monitoring AI news, research papers, and repositories. Uses **Zyte** for cloud-based scraper orchestration, **Scrapy** for spiders, **ChromaDB** for vector storage, and **OpenAI** for embeddings and summarization.

## Architecture

```
Collectors (Scrapy Spiders)
    ↓
Zyte Jobs Dashboard (scheduling + monitoring)
    ↓
Data Processing (clean + dedupe)
    ↓
Embedding + Vector Storage (ChromaDB)
    ↓
Query Interface (CLI / API)
    ↓
Summarization + Alerts
```

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your Zyte API key, OpenAI key, etc.

# Run a spider locally
scrapy crawl openai_blog

# Deploy to Zyte
shub deploy

# Query the knowledge base
python -m api.cli "What AI model launches happened this week?"
```

## Project Structure

| Directory | Purpose |
|-----------|---------|
| `spiders/` | Scrapy spiders for each source |
| `processing/` | Data cleaning + deduplication |
| `storage/` | ChromaDB vector storage |
| `api/` | Query CLI and HTTP API |
| `summarization/` | GPT-based report generation |
| `alerting/` | Email / Slack digests |
| `config/` | Spider configs + selectors |

## Sources

- OpenAI Blog
- Google Research Blog
- Anthropic Blog
- Papers with Code (trending)
- HuggingFace Papers
- GitHub Trending Repos
- Hacker News (AI tag)
- arXiv (CS.AI, CS.LG)

## License

MIT
