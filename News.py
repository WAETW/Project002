from newsapi import NewsApiClient
from Speak import speak
import time
import speech_recognition

api = NewsApiClient(api_key='04739a6cbc43442b9c783f71b6850932')


def headlines():
    top_headlines = api.get_top_headlines(country='tw')

    return top_headlines

def articles(word):
    
    all_articles = api.get_everything(q=word)

    return all_articles

def all_news(last):
    for i in range(0,3):
        #print(top_headlines['articles'][i]['title'])
        #print(top_headlines['articles'][i]['description'])
        if last['articles'][i]['description'] == None:
            news = last['articles'][i]['title']+ '。\n'
        else:
            news = last['articles'][i]['title']+ '。\n' + last['articles'][i]['description']

        print(news)
        speak(news,'zh-TW')
        time.sleep(45)
    return news

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("請選擇搜尋方式(頭條/關鍵字)")
        speak('請選擇搜尋方式','zh-TW')
        time.sleep(2)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')

def keyword():
    w = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        w.adjust_for_ambient_noise(source, duration=5)
        print("請選擇關鍵字")
        speak('請選擇關鍵字','zh-TW')
        time.sleep(2)
        audio = w.listen(source)
        print(w.recognize_google(audio, language='zh-TW'))
    return w.recognize_google(audio, language='zh-TW')

def post(key):
    if key=='頭條':
        all_news(headlines())
    elif key=='關鍵字':
        all_news(articles(keyword()))


#post(listenTo()) ##run

#os.system("pause")
