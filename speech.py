import speech_recognition as sr
from BingTTS import TTS
import time
def speech(title,duration,i):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration)
        print(title)
        TTS(title,'中文')
        time.sleep(i)
        audio=r.listen(source)
        try:
            recognize = r.recognize_bing(audio,key="ca9c8dea98a74ef0bf98b5519a5010f3",language="zh-TW")
            print(recognize)
        except sr.UnknownValueError:
            recognize = "無法辨識!"
        except sr.UnboundLocalError:
            recognize = "無法辨識!"
    return recognize
