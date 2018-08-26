import requests
import json
from bs4 import BeautifulSoup
from googletrans import Translator
from pprint import pprint

def getweather():
    translate = Translator()
    woeid = '2306179'
    res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D' + woeid + '%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    data = json.loads(res.text)

    data = data['query']['results']['channel']

    location = data['location']

    wind = data['wind']
    speed = wind['speed']

    atmosphere = data['atmosphere']
    humidity = atmosphere['humidity']
    visibility = atmosphere['visibility']
    pressure = atmosphere['pressure']

    astronomy = data['astronomy']
    sunrise = astronomy['sunrise']
    sunset = astronomy['sunset']

    location = location['city']+' ,'+location['country']
    location = translate.translate(text=location,src='en',dest='zh-TW')

    item = data['item']
    temp = item['condition']['temp']
    condition = translate.translate(text=item['condition']['text'],src='en',dest='zh-TW')
    date = translate.translate(text=item['condition']['date'],src='en',dest='zh-TW')

    print(location.text)
    print('風速：' + speed +' 公里/小時')
    print('濕度：' + humidity + '%\n' + '能見度：' + visibility + '公里\n' + '氣壓：' + pressure + '毫巴')
    print('日出時間：' + sunrise + '\n日落時間；' + sunset)
    print('溫度：' + temp + '°C\n' + '天氣狀況：' + condition.text + '\n資料時間：' + date.text)
