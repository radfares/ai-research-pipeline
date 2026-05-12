"""Clean and normalize scraped text."""
import re

def clean_text(raw):
    t = re.sub(r'<[^>]+>', ' ', raw)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()
