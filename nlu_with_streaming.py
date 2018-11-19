from weather import *
from News import *
from spotify_playback_control import spotifycontrol
from BingTTS import *
from translate import *
from read_gmail import *
import random
'''開啟麥克風並透過Dialogflow內建的語音辨識功能來辨識'''
def detect_intent_stream():
    session = random.randint(0,10)
    import dialogflow_v2 as dialogflow
    import pyaudio
    project_id = 'newagent-7ae55'
    session_id = str(session)
    language_code = 'zh-TW'
    session_client = dialogflow.SessionsClient()
    audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 44000

    session_path = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session_path))

    def request_generator(audio_config):
        query_input = dialogflow.types.QueryInput(audio_config=audio_config)

        yield dialogflow.types.StreamingDetectIntentRequest(
            session=session_path, query_input=query_input,single_utterance = True)

        audio = pyaudio.PyAudio()
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44000
        CHUNK = 4096
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input_device_index = 1,input=True, frames_per_buffer=CHUNK)
        print("嗨")
        while True:
            chunk = stream.read(CHUNK,exception_on_overflow = False)
            if not chunk:
                break
            yield dialogflow.types.StreamingDetectIntentRequest(
                input_audio=chunk,single_utterance = True)
        stream.stop_stream()
        stream.close()
        audio.terminate()

    audio_config = dialogflow.types.InputAudioConfig(
        audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)

    requests = request_generator(audio_config)
    responses = session_client.streaming_detect_intent(requests)

    print('=' * 20)
    for response in responses:
        print('Intermediate transcript: "{}".'.format(
                response.recognition_result.transcript))

    query_result = response.query_result

    print('=' * 20)
    print('語音辨識結果: {}'.format(query_result.query_text))
    print('動作: {} (confidence: {})\n'.format(
        query_result.intent.display_name,
        query_result.intent_detection_confidence))
    return response
'''處理Agent所回傳的Response'''
def action_detection(response):
    action = response.query_result.action
    if action == "weather-search":
        spotify_auth_check = spotifycontrol('暫停','')
        location = format(response.query_result.parameters['Taiwan-city'])
        date = format(response.query_result.parameters['date'])
        print(date)
        if date == "":
            weather_current(location)
        else:
            weather_forecast(date,location)
    elif action == "music-play":
        music_action = format(response.query_result.parameters['music-action'])
        music_category= format(response.query_result.parameters['music-category'])
        music_artist = format(response.query_result.parameters['music-artist'])
        if music_action == "播放":
            if music_category == "" and music_artist == "":
                music_category_null = ""
                spotify_auth_check = spotifycontrol(music_action,music_category_null)
                if spotify_auth_check == False:
                   translate("未登入","中文") 
            elif music_artist == "":
                spotify_auth_check = spotifycontrol("搜尋播放清單",music_category)
                if spotify_auth_check == False:
                   translate("未登入","中文")
            elif music_category == "":
                spotify_auth_check = spotifycontrol("搜尋歌手",music_artist)
                if spotify_auth_check == False:
                   translate("未登入","中文")
        else:
            spotify_auth_check = spotifycontrol(music_action,music_category)
            if spotify_auth_check == False:
                   translate("未登入","中文")
    elif action == "news-broadcast":
        spotify_auth_check = spotifycontrol('暫停','')
        new_action = format(response.query_result.parameters['news-action'])
        new_category = format(response.query_result.parameters['news-category'])
        if new_category == "頭條":
            all_news(headlines())
        else:
            print("我不懂")
    elif action == "news-keyword":
        spotify_auth_check = spotifycontrol('暫停','')
        news_text = format(response.query_result.parameters['any'])
        if news_text == "":
            TTS("我不懂","中文")
        else:
            all_news(articles(news_text))
    elif action == "translate.text":
        spotify_auth_check = spotifycontrol('暫停','')
        language_to = format(response.query_result.parameters['translate-language'])
        text = format(response.query_result.parameters['text'])
        if(language_to == '' or text == ''):
            TTS("我不懂","中文")
        else:
            translate(text,language_to)
        translate(text,language_to)
    elif action == "readmail":
        spotify_auth_check = spotifycontrol('暫停','')
        read_gmail()
    elif action == "input.unknown":
        spotify_auth_check = spotifycontrol('暫停','')
        translate("我不懂","中文")       
    else:
        spotify_auth_check = spotifycontrol('暫停','')
        translate("我不懂","中文")
def main():
    response = detect_intent_stream()
    action_detection(response)
if __name__ == "__main__":
    main()

