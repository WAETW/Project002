import spotipy
import speech_recognition as sr
import os
import spotipy.util as util
from json.decoder import JSONDecodeError

scope = ''
username = ""
client_id=''
client_secret=''
redirect_uri=''

try:
    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

sp = spotipy.Spotify(auth=token)
devices = sp.devices()
deviceID = devices['devices'][0]['id']
deviceName = devices['devices'][0]['name']
#目前播放
def nowplaying():
    track = sp.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    nowplay = "目前播放:"+ artist + " - " + track
    return print(nowplay)
#歌曲搜尋
def searchsong(q):
    track = sp.search(q, limit=1, offset=0, type='track', market='TW')
    artist = track['tracks']['items'][0]['artists'][0]['name']
    album = track['tracks']['items'][0]['album']['name']
    track = track['tracks']['items'][0]['name']
    searchresult = "搜尋結果:"+ artist + " - " + album + " - " + track
    return print(searchresult)
#控制
def spotifycontrol(seq):
    if seq == "目前播放":
        nowplaying()
    elif seq == "暫停":
        sp.pause_playback(deviceID)
    elif seq == "下一首":
        sp.next_track(deviceID)
    elif seq == "上一首":
        sp.previous_track(deviceID)
    elif seq == "搜尋":
