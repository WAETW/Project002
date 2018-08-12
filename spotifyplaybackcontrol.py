import spotipy
import spotipy.util as util

scope = 'user-read-private user-read-playback-state user-modify-playback-state'

username = ""
#API認證
token = util.prompt_for_user_token(username,scope,client_id='',client_secret='',redirect_uri='')


if token:
    #建立物件
    sp = spotipy.Spotify(auth=token)
    #取得撥放平台ID
    devices = sp.devices()
    deviceID = devices['devices'][0]['id']
    deviceName = devices['devices'][0]['name']
    #取得目前翻放內容
    track = sp.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    print("播放於:"+deviceName)
    print("目前撥放 " + artist + " - " + track)
    #歌曲暫停
    sp.pause_playback(deviceID)
    print("歌曲已暫停")
else:
    print ("Can't get token for", username)
