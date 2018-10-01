from googletrans import Translator
import speech_recognition
from Speak import speak
#import time
from speech import speech
from BingTTS import TTS

#翻譯
def translate(l):
    translate = Translator()

    if l == '':
        TTS('要翻譯成什麼語言','中文')
        l = speech('要翻譯成什麼語言',2,2)

    TTS('我正在聽','中文')
    #say = speech('我正在聽',2,2)
    say = '你好嗎'
    result = translate.translate(say ,dest=lan.get(l))
    #result = translate.translate(say ,dest=lan.get('日文'))
    #result = translate.translate('我想吃晚餐',dest=lan.get('日文'))

    #speak(result.text,lan.get(l))
    TTS(result.text,l)
    #print (result.text)
    return result.text

#翻譯語言
lan = {
    '英文':'en',
    '中文':'zh-TW',
    '日文':'ja'
}

#translate(None)
#translate('日文','你好嗎')
#translate(speech('請選擇要翻譯的語言',2,3), speech('正在翻譯...',2,2))
