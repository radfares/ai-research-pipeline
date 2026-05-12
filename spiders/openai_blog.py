import scrapy
from spiders.items import ArticleItem
from datetime import datetime

class OpenAISpider(scrapy.Spider):
    name = "openai_blog"
    source = "OpenAI Blog"
    item_type = "article"
    start_urls = ["https://openai.com/news"]

    def parse(self, response):
        for post in response.css("a[href*='/news/']"):
            url = response.urljoin(post.css("::attr(href)").get(""))
            title = post.css("::text").get("") or ""
            yield response.follow(url, callback=self.parse_article, meta={"title": title.strip()})

    def parse_article(self, response):
        item = ArticleItem()
        item["title"] = response.meta.get("title") or response.css("h1::text").get("")
        item["url"] = response.url
        item["source"] = self.source
        item["published"] = response.css("time::attr(datetime)").get("")
        paragraphs = response.css("article p, .post-content p, .prose p")
        item["cleaned_text"] = "\n".join(p.css("::text").get("") for p in paragraphs)
        item["tags"] = ["ai", "openai", "blog"]
        item["scraped_at"] = datetime.utcnow().isoformat()
        yield item
