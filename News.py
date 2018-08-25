from newsapi import NewsApiClient
from Speak import speak
import time
api = NewsApiClient(api_key='04739a6cbc43442b9c783f71b6850932')


def headlines():
    top_headlines = api.get_top_headlines(country='tw')

    for i in range(0,2):
        #print(top_headlines['articles'][i]['title'])
        #print(top_headlines['articles'][i]['description'])
        news = top_headlines['articles'][i]['title']+ '\n' + top_headlines['articles'][i]['description']

        print(news)
        speak(news,'zh-TW')
        time.sleep(45)
    return news





headlines()
#speak(headlines(),'zh-TW')
#os.system("pause")
