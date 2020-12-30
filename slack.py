from datetime import date, timedelta
import json
import sys

from slacker import Slacker

def post_message():
    with open('test.json', 'r') as json_file:
        INFO = json.load(json_file)

    with open('config.json', 'r') as json_file:
        CONFIG = json.load(json_file)

    slack = Slacker(CONFIG['token'])

    yesterday = str(date.today() - timedelta(1))

    attachments_dict = dict()
    attachments_dict['pretext'] = '코로나 확진자 알림'
    attachments_dict['title'] = f'[{yesterday}]'
    attachments_dict['title_link'] = 'http://ncov.mohw.go.kr/'
    attachments_dict['fallback'] = f'[{yesterday}] 코로나 확진자 알림'
    attachments_dict['text'] = f"""*누적*: {INFO["total"]}명
    *소계*: {INFO["sub_total"]}명
    *국내발생*: {INFO["local"]}명
    *해외유입*: {INFO["inflow"]}명"""
    attachments = [attachments_dict]

    slack.chat.post_message(channel=CONFIG['channel'], text=None, attachments=attachments, as_user=True)
