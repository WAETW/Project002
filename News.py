from newsapi import NewsApiClient
#from Speak import speak
#import time
#import speech_recognition
from BingTTS import TTS

api = NewsApiClient(api_key='04739a6cbc43442b9c783f71b6850932')

def headlines():
    top_headlines = api.get_top_headlines(country='tw')
    return top_headlines

def articles(word):
    all_articles = api.get_everything(q=word)
    return all_articles

def all_news(last):
    #ticks=time.time()
    #print(ticks)
    for i in range(0,3):
        #print(top_headlines['articles'][i]['title'])
        #print(top_headlines['articles'][i]['description'])
        if last['articles'][i]['description'] == None:
            news = last['articles'][i]['title']+ '。\n'
        else:
            news = last['articles'][i]['title']+ '。\n' + last['articles'][i]['description']+ '。\n'
        #print(news)
        TTS(news,'中文')

    #ticks2=time.time()
    #print(ticks2-ticks)
    return news

def post(key):
    if key=='頭條':
        all_news(headlines())
    elif key=='關鍵字':
        all_news(articles(keyword()))

##def test():
##    for i in range(0,1):
##      last = api.get_top_headlines(category='sports',country='tw')
##        news = last['articles'][i]['title']+ '。\n' + last['articles'][i]['description']
##        print(news)

#post(listenTo()) ##run
#all_news(articles('颱風'))
#os.system("pause")
