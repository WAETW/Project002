from speech import speech
from spotify_playback_control import spotifycontrol
from weather import getweather
from translate import *
from News import *

command = speech("請說:",5)
if command == "音樂":
    subcommand = speech("使用spotify:",5)
    spotifycontrol(subcommand)
elif command == "翻譯":
    translate(langue(), translateTo())
elif command == "天氣":
    getweather()
elif command == "新聞":
    post(listenToNews())
else:
    print("...")
