import tempfile
import wave
from pydub import AudioSegment
import pyaudio

def wavplay(sound):
    print(sound)
    #mp3 to wav
    #AudioSegment.from_mp3(sound).export(("{}.wav".format(fp.name)), format="wav")
    #play wav
    chunk=1024
    file =(sound)
    print(file)
    f = wave.open(file,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
            channels = f.getnchannels(),
            rate = f.getframerate(),
            output = True)
    data = f.readframes(chunk)
    while len(data)>0:
    #while data != "":
    #while True:
        stream.write(data)
        data = f.readframes(chunk)
    #stream.stop_stream()
    stream.close()
    p.terminate()
    #end
