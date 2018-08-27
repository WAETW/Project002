from speech import speech
from spotify_playback_control import spotifycontrol
from weather import getweather
from translate import *
from News import *

command = speech()
if command == "音樂":
    subcommand = speech()
    spotifycontrol(subcommand)
elif command == "翻譯":
    trasnlate(langue(), listenTo())
elif command == "天氣":
    getweather()
elif command == "新聞":
    post(listenTo())
else:
    print("...")
