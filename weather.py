import requests
import json
import time
import datetime
import dateutil.parser
from BingTTS import TTS

#set woeid
woeid = dict(臺北='2306179',
新北='20070569',
基隆='2306188',
桃園='2298866',
新竹='2306185',
苗栗='2301128',
臺中='2306181',
彰化='2306183',
南投='2306204',
雲林='2347346',
嘉義='2296315',
臺南='2306182',
高雄='2306180',
屏東='2306189',
宜蘭='2306198',
花蓮='2306187',
臺東='2306190')


def weather_current(city):
    if city in woeid:
        #load weather's json file
        res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D' + woeid.get(city) + '%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
        data = json.loads(res.text)

        data = data['query']['results']['channel']

        atmosphere = data['atmosphere']
        humidity = atmosphere['humidity']

        item = data['item']
        temp = item['condition']['temp']
        #print results
        print('溫度：' + temp + '°C' + ' 濕度：' + humidity + '% 天氣狀況：' + item['condition']['text'])
        TTS('溫度：' + temp + '°C' + ' 濕度：' + humidity + '% 天氣狀況：' + item['condition']['text'],'中文')
    else:
        TTS('我不懂','中文')
def weather_forecast(date,city):
    if city in woeid:
        #處理dialogflow的Timestamp
        json_to_date = dateutil.parser.parse(date, ignoretz=True).strftime("%d %b %Y")
        print(json_to_date)

        #load weather's json file
        res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D' + woeid.get(city) + '%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')# + woeid.get(city))
        data = json.loads(res.text)
        forecast = data['query']['results']['channel']['item']['forecast']

        #print results
        for i in range(len(forecast)) :
            if json_to_date == forecast[i]['date']:
                print('氣溫：' + forecast[i]['high'] + '°C~' + forecast[i]['low'] + '°C 天氣狀況：' + forecast[i]['text'])
                TTS('氣溫：' + forecast[i]['high'] + '°C~' + forecast[i]['low'] + '°C 天氣狀況：' + forecast[i]['text'],'中文')
    else:
        TTS('我不懂','中文')
#weather_current('臺中')
