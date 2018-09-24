from googletrans import Translator
import speech_recognition
from Speak import speak
import time


#翻譯
def translate(l,say):
    translate = Translator()
    result = translate.translate(say ,dest=lan.get(l))
    #result = translate.translate(say ,dest=lan.get('日文'))
    #result = translate.translate('我想吃晚餐',dest=lan.get('日文'))

    speak(result.text,lan.get(l))
    time.sleep(10)
    print (result.text)
    return result.text

#翻譯語言
lan = {
    '英文':'en',
    '中文':'zh-TW',
    '日文':'ja'
}

#translate('日文','你好嗎')
#translate(speech('請選擇要翻譯的語言',2,3), speech('正在翻譯...',2,2))
