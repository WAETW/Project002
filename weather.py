import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

woeid = '2306179'
res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D' + woeid + '%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
data = json.loads(res.text)

data = data['query']['results']['channel']

location = data['location']
wind = data['wind']
atmosphere = data['atmosphere']
astronomy = data['astronomy']
item = data['item']

location = location['city']+' ,'+location['country']
wind = wind['speed']

print(location)
print('風速：' + wind +' 公里/小時')
print('濕度：' + atmosphere['humidity'] + '%\n' + '能見度：' + atmosphere['visibility'] + '公里\n' + '氣壓：' + atmosphere['pressure'] + '毫巴')
print('日出時間：' + astronomy['sunrise'] + '\n日落時間；' + astronomy['sunset'])
print('溫度：' + item['condition']['temp'] + '°C\n' + '天氣狀況：' + item['condition']['text'] + '\n資料時間：' + item['condition']['date'])
