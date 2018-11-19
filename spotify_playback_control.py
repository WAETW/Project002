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
def exception_handling():
    try:
        devices = sp.devices()
        device = devices['devices'][0]['is_active']
        for i in range(0,3):
            if devices['devices'][i]['name'] == 'test-1':
                deviceID = devices['devices'][i]['id']
                current_volume = devices['devices'][i]['volume_percent']
                print(deviceID)
                return True, deviceID, current_volume
    except IndexError:
        deviceIDs = ''
        current_volume = ''
        return False, deviceID, current_volume
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
def searchsong(q,deviceID):
    track = sp.search(q, limit=1, offset=0, type='track', market='TW')
    artist = track['tracks']['items'][0]['artists'][0]['name']
    album = track['tracks']['items'][0]['album']['name']
    trackname = track['tracks']['items'][0]['name']
    trackuri = track['tracks']['items'][0]['uri']
    searchresult = "搜尋結果:"+ artist + " - " + album + " - " + trackname
    tracklist = []
    tracklist.append(trackuri)
    sp.start_playback(deviceID, context_uri=None, uris=tracklist, offset=None)
#搜尋播放清單並播放
def searchplaylist(q,deviceID):
    playlist = sp.search(q, limit=1, offset=0, type='playlist', market='TW')
    playlisturi = playlist['playlists']['items'][0]['uri']
    sp.start_playback(deviceID, context_uri=playlisturi, uris=None, offset=None)
#搜尋歌手
def searchartist(q,deviceID):
    playlist = sp.search(q, limit=1, offset=0, type='playlist', market='TW')
    playlisturi = playlist['playlists']['items'][0]['uri']
    sp.start_playback(deviceID, context_uri=playlisturi, uris=None, offset=None)

#繼續播放
def resume(deviceID):
    track = sp.current_user_playing_track()
    status = track['is_playing']
    if status == False:
        sp.start_playback(deviceID, context_uri=None, uris=None, offset=None)

#控制
def spotifycontrol(seq,search):
    auth_tag, deviceID, current_volume = exception_handling()
    print(auth_tag)
    if auth_tag == False:
        print('==')
        return False  
    if seq == "目前播放":
        print(nowplaying())
    elif seq == "暫停":
        track = sp.current_user_playing_track()
        status = track['is_playing']
        if status == True:
            sp.pause_playback(deviceID)
        return True
    elif seq == "下一首":
        sp.next_track(deviceID)
        return True
    elif seq == "上一首":
        sp.previous_track(deviceID)
        return True
    elif seq == "搜尋播放清單":
        searchplaylist(search,deviceID)
        return True
    elif seq == "搜尋歌手":
        searchartist(search,deviceID)
        return True
    elif seq == "大聲點":
        set_volume = current_volume + 10
        sp.volume(set_volume,deviceID)
        return True
    elif seq == "小聲點":
        set_volume = current_volume -10
        sp.volume(set_volume,deviceID)
        return True
    elif seq == "播放":
        resume(deviceID)
        return True
    else:
        print("我不懂")
        return True
def main():
    spotifycontrol('暫停','')
if __name__ == '__main__':
    main()