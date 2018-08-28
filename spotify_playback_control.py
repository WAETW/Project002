import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
from speech import speech

scope = 'user-read-private user-read-playback-state user-modify-playback-state'
username = "呂晟暐"

try:
    token = util.prompt_for_user_token(username,scope)
except (AttributeError, JSONDecodeError):
    #os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope)

sp = spotipy.Spotify(auth=token)
devices = sp.devices()
#deviceID = devices['devices'][0]['id']
deviceID = '98bb0735e28656bac098d927d410c3138a4b5bca'
deviceName = devices['devices'][0]['name']
current_volume = devices['devices'][0]['volume_percent']
#播放狀態
def playing_status():
    track = sp.current_user_playing_track()
    status = track['is_playing']
    return status
#目前播放
def nowplaying():
    track = sp.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    nowplay = "目前播放:"+ artist + " - " + track
    return nowplay
#歌曲搜尋並播放
def searchsong(q):
    track = sp.search(q, limit=1, offset=0, type='track', market='TW')
    artist = track['tracks']['items'][0]['artists'][0]['name']
    album = track['tracks']['items'][0]['album']['name']
    trackname = track['tracks']['items'][0]['name']
    trackuri = track['tracks']['items'][0]['uri']
    searchresult = "搜尋結果:"+ artist + " - " + album + " - " + trackname
    tracklist = []
    tracklist.append(trackuri)
    sp.start_playback(deviceID, context_uri=None, uris=tracklist, offset=None)
    #return print(searchresult)
#搜尋播放清單並播放
def searchplaylist(q):
    playlist = sp.search(q, limit=1, offset=0, type='playlist', market='TW')
    playlisturi = playlist['playlists']['items'][0]['uri']
    sp.start_playback(deviceID, context_uri=playlisturi, uris=None, offset=None)
#繼續播放
def resume():
    sp.start_playback(deviceID, context_uri=None, uris=None, offset=None)
#控制
def spotifycontrol(seq):
    if seq == "目前播放":
        print(nowplaying())
    elif seq == "暫停":
        sp.pause_playback(deviceID)
    elif seq == "下一首":
        sp.next_track(deviceID)
    elif seq == "上一首":
        sp.previous_track(deviceID)
    elif seq == "搜尋歌曲":
        search = speech("輸入歌名:",5,1)
        if search == "無法辨識!":
            print("無法辨識!")
        else:
            searchsong(search)
    elif seq == "搜尋播放清單":
        search = speech("輸入清單名稱:",5,2)
        if search == "無法辨識!":
            print("無法辨識!")
        else:
            searchplaylist(search)
    elif seq == "大聲點":
        set_volume = current_volume + 10
        sp.volume(set_volume,deviceID)
    elif seq == "小聲點":
        set_volume = current_volume -10
        sp.volume(set_volume,deviceID)
    elif seq == "繼續播放":
        resume()
