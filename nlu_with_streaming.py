from weather import *
from News import *
from spotify_playback_control import spotifycontrol
from BingTTS import *
from translate import *
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
        '''print('Intermediate transcript: "{}".'.format(
                response.recognition_result.transcript))'''

    query_result = response.query_result

    print('=' * 20)
    print('Query text: {}'.format(query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        query_result.intent.display_name,
        query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        query_result.fulfillment_text))
    return response
'''處理Agent所回傳的Response'''
def action_detection(response):
    action = response.query_result.action
    print(action)
    if action == "weather-search":
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
                spotifycontrol(music_action,music_category_null)
            elif music_artist == "":
                spotifycontrol("搜尋播放清單",music_category)
            elif music_category == "":
                spotifycontrol("搜尋歌手",music_artist)
        else:
            spotifycontrol(music_action,music_category)
    elif action == "news-broadcast":
        new_action = format(response.query_result.parameters['news-action'])
        new_category = format(response.query_result.parameters['news-category'])
        if new_category == "頭條":
            post("頭條")
        else:
            print("我不懂")
    elif action == "translater":
        translate_action = format(response.query_result.parameters['translate-action'])
        translate_language = format(response.query_result.parameters['translate-language1'])
        translate(translate_language)
    elif action == "translate.text":
        language_to = format(response.query_result.parameters['translate-language'])
        text = format(response.query_result.parameters['text'])
        translate(text,language_to)
    elif action == "input.unknown":
        TTS("我不懂","中文")
'''def main():
    response = detect_intent_stream()
    action_detection(response)
if __name__ == "__main__":
    main()'''
