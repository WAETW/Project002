import snowboydecoder
import signal
from nlu_with_streaming import *
from wav import *
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def detected():
    detector.terminate()
    snowboydecoder.play_audio_file("咕嚕靈波.wav")
    response = detect_intent_stream()
    action_detection(response)
    detector.start(detected_callback=detected,interrupt_check=interrupt_callback,sleep_time=0.03)



model = "小白.pmdl"
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
#print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detected,interrupt_check=interrupt_callback,sleep_time=0.03)

detector.terminate()
