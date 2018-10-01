import dialogflow
from weather import getweather
from News import *
from spotify_playback_control import spotifycontrol
from Speak import speak 


def detect_intent_texts(input):
    project_id = "newagent-7ae55"
    session_id = "1"
    language_code = "zh-TW"
    texts = []
    texts.append(input)
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        def action_detection(action):
            print(action)
            if action == "weather-search":
                location = format(response.query_result.parameters['Taiwan-city'])
                getweather(location)
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
            elif action == "input.unknown":
                speak("我不懂","zh-tw")
        action_detection(format(response.query_result.action))
        

