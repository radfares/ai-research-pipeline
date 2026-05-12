# Scrapy items for AI Research Pipeline
import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    published = scrapy.Field()
    source = scrapy.Field()
    cleaned_text = scrapy.Field()
    raw_html = scrapy.Field()
    scraped_at = scrapy.Field()
    tags = scrapy.Field()

class PaperItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    authors = scrapy.Field()
    abstract = scrapy.Field()
    published = scrapy.Field()
    source = scrapy.Field()
    cleaned_text = scrapy.Field()
    scraped_at = scrapy.Field()
    tags = scrapy.Field()

class RepoItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    owner = scrapy.Field()
    description = scrapy.Field()
    stars = scrapy.Field()
    language = scrapy.Field()
    source = scrapy.Field()
    cleaned_text = scrapy.Field()
    scraped_at = scrapy.Field()
    tags = scrapy.Field()
