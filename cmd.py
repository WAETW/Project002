from speech import speech
from spotify_playback_control import *
from weather import getweather
from translate import *
from News import *

temp_status = False
if playing_status() == True:
    temp_status = playing_status()
    spotifycontrol("暫停")
command = speech("嗨!",2,1)
if command == "音樂":
    subcommand = speech("請輸入指令:",2,2)
    if temp_status == True:
        resume()
    spotifycontrol(subcommand)
elif command == "翻譯":
    translate(speech('請選擇要翻譯的語言',2,3), speech('正在翻譯...',2,2))
    if temp_status == True:
        resume()
elif command == "天氣":
    getweather()
    if temp_status == True:
        resume()
elif command == "新聞":
    post(speech('請選擇搜尋方式',2,2))
    if temp_status == True:
        resume()
else:
    print("...")
