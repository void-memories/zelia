import time
from playsound import playsound
from threading import Thread
import getch


def metronome():
    while 1:
        playsound('chordWavs/stick.wav',False)
        time.sleep(2.5/4)

def chords():
    queue=['F','Am','C','G']
    while 1:
        for i in queue:
            playsound(f"chordWavs/90BPM/{getch.getche()}.wav",False)
            #2==120BPM
            #2.5==90BPM

if __name__ == '__main__':
    # Thread(target = metronome).start()
    Thread(target = chords).start()
