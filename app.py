import datetime
import json
import os
import sys

import scrapy
from scrapy.crawler import CrawlerProcess

from covid19 import Covid19Spider

today = datetime.date.today()
today = f'{int(today.month)}.{int(today.day)}'

if os.path.exists('covid19.json'):
    with open('covid19.json', 'r') as json_file:
        INFO = json.load(json_file)

    if INFO['date'] == today:
        print(f'INFO["date"]: {INFO["date"]}, today: {today}')
        sys.exit(1)

process = CrawlerProcess()
process.crawl(Covid19Spider)
process.start()
