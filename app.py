import scrapy
from scrapy.crawler import CrawlerProcess

from covid19 import Covid19Spider

process = CrawlerProcess()
process.crawl(Covid19Spider)
process.start()
