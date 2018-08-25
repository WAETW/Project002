import speech_recognition as sr

def speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("請說:")
        audio=r.listen(source)
        try:
            recognize = r.recognize_google(audio, language="zh-TW")
            print(recognize)
        except sr.UnknownValueError:
            print("無法辨識!")
    return recognize
