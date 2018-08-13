from googletrans import Translator
import speech_recognition


def listenTo():
    sen = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        sen.adjust_for_ambient_noise(source, duration=5)
        audio = sen.listen(source)
        print('Say something')
        print(sen.recognize_google(audio, language='zh-TW'))
    return sen.recognize_google(audio, language='zh-TW')


def speak(sentence):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-TW')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

def translate():
    translate = Translator()
    result = translate.translate(sen.recognize_google(audio, language='zh-TW') ,dest=lan.get('日文'))

    print (result.text)
    return result.text


lan = {
    '英文':'en',
    '中文':'zh-TW',
    '日文':'ja'
}


translate(listenTo())

