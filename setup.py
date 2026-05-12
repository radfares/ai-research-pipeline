"""Package setup for AI Research Pipeline."""
from setuptools import setup, find_packages

setup(
    name="ai-research-pipeline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scrapy>=2.11.0",
        "zyte-api>=0.7.2",
        "chromadb>=0.5.0",
        "openai>=1.30.0",
        "fastapi>=0.111.0",
        "uvicorn>=0.30.0",
        "schedule>=1.2.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "airp-query=api.cli:main"
        ]
    }
)
