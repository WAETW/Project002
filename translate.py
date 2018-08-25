from googletrans import Translator
import speech_recognition
from Speak import speak

def listenTo():
    sen = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        sen.adjust_for_ambient_noise(source, duration=5)
        speak('正在翻譯...','zh-TW')
        print('正在翻譯...')
        audio = sen.listen(source)
        print(sen.recognize_google(audio, language='zh-TW'))

    return sen.recognize_google(audio, language='zh-TW')

def langue():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)

        speak('請選擇要翻譯的語言','zh-TW')
        print('請選擇要翻譯的語言(英/中/日)')

        audio = r.listen(source)
        print(r.recognize_google(audio, language='zh-TW'))
       
    return r.recognize_google(audio, language='zh-TW')


def translate(l,say):
    translate = Translator()
    result = translate.translate(say ,dest=lan.get(l))
    #result = translate.translate(say ,dest=lan.get('日文'))
    #result = translate.translate('我想吃晚餐',dest=lan.get('日文'))
    
    speak(result.text,lan.get(l))
    print (result.text)
    return result.text
    

lan = {
    '英文':'en',
    '中文':'zh-TW',
    '日文':'ja'
}

#translate('日文','你好嗎')
#translate(langue(),listenTo())
#speak(translate(langue(),listenTo()),r.recognize_google(audio, language='zh-TW'))
