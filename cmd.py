from speech import speech
from spotify_playback_control import spotifycontrol
import translate

command = speech()
if command == "音樂":
    subcommand = speech()
    spotifycontrol(subcommand)
elif command == "翻譯":
    trasnlate(langue(), listenTo())
else:
    print("...")
