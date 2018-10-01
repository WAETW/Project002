import speech_recognition as sr
def speech(title,duration):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration)
        print(title)
        audio=r.listen(source)
        try:
            recognize = r.recognize_bing(audio,key="ca9c8dea98a74ef0bf98b5519a5010f3",language="zh-TW")
            print(recognize)
        except sr.UnknownValueError:
            recognize = "無法辨識!"
        except sr.UnboundLocalError:
            recognize = "無法辨識!"
    return recognize

