from speech import speech
from spotify_playback_control import spotifycontrol

command = speech()
if command == "音樂":
    subcommand = speech()
    spotifycontrol(subcommand)
else:
    print("...")
