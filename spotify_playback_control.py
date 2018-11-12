import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError

scope = 'user-read-private user-read-playback-state user-modify-playback-state'
username = "呂晟暐"

try:
    token = util.prompt_for_user_token(username,scope)
except (AttributeError, JSONDecodeError):
    token = util.prompt_for_user_token(username,scope)

sp = spotipy.Spotify(auth=token)
auth_tag = False
try:
    devices = sp.devices()
    deviceID = devices['devices'][0]['id']
    current_volume = devices['devices'][0]['volume_percent']
    auth_tag = True
except IndexError:
    print('= =')
    auth_tag = False
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
#搜尋歌手
def searchartist(q):
    playlist = sp.search(q, limit=1, offset=0, type='playlist', market='TW')
    playlisturi = playlist['playlists']['items'][0]['uri']
    sp.start_playback(deviceID, context_uri=playlisturi, uris=None, offset=None)

#繼續播放
def resume():
    track = sp.current_user_playing_track()
    status = track['is_playing']
    if status == False:
        sp.start_playback(deviceID, context_uri=None, uris=None, offset=None)

#控制
def spotifycontrol(seq,search):
    if auth_tag== False:
        print('==')
        return    
    if seq == "目前播放":
        #speak(nowplaying(),zh-tw)
        print(nowplaying())
    elif seq == "暫停":
        track = sp.current_user_playing_track()
        status = track['is_playing']
        if status == True:
            sp.pause_playback(deviceID)
    elif seq == "下一首":
        sp.next_track(deviceID)
    elif seq == "上一首":
        sp.previous_track(deviceID)
    elif seq == "搜尋播放清單":
        searchplaylist(search)
    elif seq == "搜尋歌手":
        searchartist(search)
    elif seq == "大聲點":
        set_volume = current_volume + 10
        sp.volume(set_volume,deviceID)
    elif seq == "小聲點":
        set_volume = current_volume -10
        sp.volume(set_volume,deviceID)
    elif seq == "播放":
        resume()
    else:
        print("我不懂")
def main():
    spotifycontrol('暫停','')
if __name__ == '__main__':
    main()