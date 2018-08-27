import requests
import json
from bs4 import BeautifulSoup
from googletrans import Translator
import speech_recognition
from pprint import pprint
from Speak import speak
import time

def getweather():
    s = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        s.adjust_for_ambient_noise(source, duration=1)
        speak('請說出要查詢的城市','zh-tw')
        print('請說出要查詢的城市')
        time.sleep(4)
        audio = s.listen(source)
        a = s.recognize_google(audio, language='zh-TW')
        city = '' + a
    woeid = dict(台北='2306179',
    新北='20070569',
    基隆='2306188',
    桃園='2298866',
    新竹='2306185',
    苗栗='2301128',
    台中='2306181',
    彰化='2306183',
    南投='2306204',
    雲林='2347346',
    嘉義='2296315',
    台南='2306182',
    高雄='2306180',
    屏東='2306189',
    宜蘭='2306198',
    花蓮='2306187',
    台東='2306190')
    translate = Translator()
    res = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D' + woeid.get(city) + '%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
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
    #print('風速：' + speed +' 公里/小時')
    #print('濕度：' + humidity + '%\n' + '能見度：' + visibility + '公里\n' + '氣壓：' + pressure + '毫巴')
    #print('日出時間：' + sunrise + '\n日落時間；' + sunset)
    #print('溫度：' + temp + '°C\n' + '天氣狀況：' + condition.text + '\n資料時間：' + date.text)
    weather = '溫度：' + temp + '°C' + '濕度：' + humidity + '天氣狀況：' + condition.text
    speak(weather , 'zh-tw')
    time.sleep(10)
