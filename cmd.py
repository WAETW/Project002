from speech import speech
from spotify_playback_control import *
from weather import getweather
from translate import *
from News import *

if playing_status() == True:
    spotifycontrol("暫停")
command = speech("嗨!",5,1)
if command == "音樂":
    subcommand = speech("請輸入指令:",5,2)
    spotifycontrol(subcommand)
elif command == "翻譯":
    translate(speech('請選擇要翻譯的語言',5,3), speech('正在翻譯...',5,2))
elif command == "天氣":
    getweather()
elif command == "新聞":
    post(speech('請選擇搜尋方式',5,2))
else:
    print("...")
