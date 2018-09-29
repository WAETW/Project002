import dialogflow
from weather import getweather
from spotify_playback_control import spotifycontrol
from speech import speech
from News import *
def detect_intent_texts(input):
    project_id = "newagent-7ae55"
    session_id = "1"
    language_code = "zh-TW"
    texts = []
    texts.append(input)
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        #print('JSON: {}\n'.format(response))
        def action_detection(action):
            if action == "weather-search":
                location = format(response.query_result.parameters['Taiwan-city'])
                #print(location)
                getweather(location)
            elif action == "music-play":
                music_action = format(response.query_result.parameters['music-action'])
                print(music_action)
                music_category= format(response.query_result.parameters['music-category'])
                print(music_category)
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
                print("幹你娘不知道啦") #派三小


        action_detection(format(response.query_result.action))
        #print(format(response.query_result.parameters['Taiwan-city'][0])) 讀取城市
        #location = format(response.query_result.parameters['Taiwan-city'][0])
        #print(location)
        #getweather(location)
        #print('Fulfillment text: {}\n'.format(response))
        #print(format(response.query_result.parameters['music-action'][0]))
        #print('Fulfillment text: {}\n'.format(response.query_result.action))


#command = speech("嗨!",2,1)
#command = "音樂暫停"
#detect_intent_texts(command)
detect_intent_texts("天佑臺中")
