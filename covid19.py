import datetime
import json
import os

import scrapy

import slack


class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1']
    start_urls = ['http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1']

    def parse(self, response):
        date = response.xpath('//*[@id="content"]/div/h5[1]/span/text()').extract()[0][1:].split('.')
        date = f'{date[0]}.{date[1]}'

        today = datetime.date.today()
        today = f'{int(today.month)}.{int(today.day)}'
        if date != today:
            print(f'date: {date}, today: {today}')
            return
        
        info = {
            'date': date,
            'total': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[1]/dl/dd/text()').extract()[0],
            'sub_total': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[1]/p/text()').extract()[0][2:],
            'local': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[2]/p/text()').extract()[0],
            'inflow': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[3]/p/text()').extract()[0],
            'death': response.xpath('//*[@id="content"]/div/div[2]/div[4]/ul/li[2]/dl/dd/span/text()').extract()[0][2:],
        }
        with open('covid19.json', 'w') as json_file:
            json.dump(info, json_file, indent=4)
        
        slack.post_message()
