import requests
from xml.etree import ElementTree
import os
import tempfile
#from Speak import speak
from wav import wavplay

def TTS(sentence,la):

    # 在 header 中附帶 key(金鑰)，並用 post 的方法發送 request
    headers = {'Ocp-Apim-Subscription-Key': '614602375c2a488099fdccacf0181bf0'}
    response = requests.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=headers)
    # Status Code 不是 200 就報錯
    if response.status_code != 200:
        print('取得 token 失敗')
        return

    # 取得 token(權杖)
    access_token = response.text
    # header 包含了 request 內容類型的宣吿、輸出音檔的格式、token
    # Bing Speech API 都是使用 SSML(語音合成標記語言) 來表達產生音檔的內容及語音特徵
    headers = {'Content-type': 'application/ssml+xml',
               'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm',
               'Authorization': 'Bearer ' + access_token}

    #<speak version="1.0" xml:lang="en-US"> <voice xml:lang="en-US" name="Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)"> </voice></speak>
    #<speak version="1.0" xml:lang="ja-JP"> <voice xml:lang="ja-JP" name="Microsoft Server Speech Text to Speech Voice (ja-JP, Ayumi, Apollo)"> </voice></speak>
    #<speak version="1.0" xml:lang="zh-TW"> <voice xml:lang="zh-TW" name="Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)"> </voice> </speak> /中英
    body = ElementTree.Element('speak', version='1.0')
    body.set('xml:lang',language.get(la))
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('xml:lang', language.get(la))
    voice.set('xml:gender', 'Female')
    #voice.set('name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)')
    voice.set('name', vo.get(la))

    #傳入欲轉換之文字
    voice.text = sentence

    # 發出請求下載檔案
    response = requests.post('https://speech.platform.bing.com/synthesize', data=ElementTree.tostring(body), headers=headers, stream=True)

    # Status Code 不是 200 就報錯
    if response.status_code != 200:
        print('取得音檔失敗')
        return

    # 存檔為暫存wav
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        with open('{}.wav'.format(fp.name), 'wb') as f:
            for chunk in response:
                f.write(chunk)
    sound = '{}.wav'.format(fp.name)
    #print(sound)
    #播放wav

    wavplay(sound)

language = {
    '中文' : 'zh-TW',
    '英文' : 'en-US',
    '日文' : 'ja-JP'
}
vo = {
    '中文' : 'Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)',
    '英文' : 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)',
    '日文' : 'Microsoft Server Speech Text to Speech Voice (ja-JP, Ayumi, Apollo)'
}

#TTS('気持ち悪い','日文')
