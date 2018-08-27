from speech import speech
from spotify_playback_control import spotifycontrol
from weather import getweather 
import translate

command = speech()
if command == "音樂":
    subcommand = speech()
    spotifycontrol(subcommand)
elif command == "翻譯":
    trasnlate(langue(), listenTo())
elif command == "天氣查詢":
    getweather()
else:
    print("...")
