from googletrans import Translator
from BingTTS import TTS

#翻譯
def translate(input,language_to):
    translate = Translator()

    if language_to in lan:
        
        #say = '你好嗎'
        result = translate.translate(input ,dest=lan.get(language_to))
        #result = translate.translate(say ,dest=lan.get('日文'))
        #result = translate.translate('我想吃晚餐',dest=lan.get('日文'))

        #speak(result.text,lan.get(l))
        TTS(result.text,language_to)
        #print (result.text)
        return result.text
    else:
        
        TTS('我不懂','中文')
#翻譯語言
lan = {
    '英文':'en',
    '中文':'zh-TW',
    '日文':'ja',
    '德文':'de',
    '法文':'fr',
    '韓文':'ko',
    '泰文':'th'
}
#translate(None)
translate('你好嗎','日文')
#translate(speech('請選擇要翻譯的語言',2,3), speech('正在翻譯...',2,2))
