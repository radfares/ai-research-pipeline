"""Cron-like scheduler for periodic runs."""
import schedule
import time

def run_spiders():
    from scrapy.crawler import CrawlerProcess
    from spiders.openai_blog import OpenAISpider
    process = CrawlerProcess()
    process.crawl(OpenAISpider)
    process.start()

def schedule_jobs():
    schedule.every().hour.do(run_spiders)
    while True:
        schedule.run_pending()
        time.sleep(60)
