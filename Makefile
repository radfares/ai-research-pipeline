.PHONY: install test lint crawl query summarize serve schedule

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	ruff check .

crawl:
	scrapy crawl openai_blog

query:
	python -m api.cli

summarize:
	python -m summarization.summarizer

serve:
	uvicorn api.server:app --reload --port 8000

schedule:
	python -m alerting.scheduler
