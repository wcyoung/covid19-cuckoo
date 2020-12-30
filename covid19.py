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
        date = response.xpath('//*[@id="content"]/div/h5[1]/span/text()').extract()[0][1:6]

        today = datetime.date.today().strftime('%m.%d')
        if date != today:
            print(f'date: {date}, today: {today}')
            return

        if os.path.exists('covid19.json'):
            with open('covid19.json', 'r') as json_file:
                INFO = json.load(json_file)
            
            if INFO['date'] == today:
                print(f'INFO["date"]: {INFO["date"]}, today: {today}')
                return
        
        info = {
            'date': date,
            'total': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[1]/dl/dd/text()').extract()[0],
            'sub_total': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[1]/p/text()').extract()[0][2:],
            'local': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[2]/p/text()').extract()[0],
            'inflow': response.xpath('//*[@id="content"]/div/div[2]/div[1]/ul/li[2]/dl/dd/ul/li[3]/p/text()').extract()[0],
        }
        with open('covid19.json', 'w') as json_file:
            json.dump(info, json_file, indent=4)
        
        slack.post_message()
