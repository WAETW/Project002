import speech_recognition as sr
from Speak import speak
import time
def speech(title,duration,time):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration)
        print(title)
        speak(title,'zh-tw')
        time.sleep(time)
        audio=r.listen(source)
        try:
            recognize = r.recognize_google(audio, language="zh-TW")
            print(recognize)
        except sr.UnknownValueError:
            print("無法辨識!")
    return recognize
