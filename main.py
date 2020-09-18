import time
import pygame
import pygame.midi
from playsound import playsound
from threading import Thread

speed = 1


def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number%12]

def update():
    global speed
    while 1:
        speed = float(input('new tempo '))


def chords():
    global speed
    queue = ['F', 'Am', 'C', 'G']
    while 1:
        for i in queue:
            playsound(f'chordWavs/90BPM/{i}.wav', False)
            time.sleep(speed)
            # time.sleep(2.5)
            # 2==120BPM
            # 2.5==90BPM


def notes():
    global speed
    chordsToNotes = {
        'C': ['C', 'E', 'G'],
        'Dm': ['D', 'F', 'A'],
        'Em': ['E', 'G', 'B'],
        'F': ['F', 'A', 'C'],
        'G': ['G', 'B', 'D'],
        'Am': ['A', 'C', 'E'],
        'B': ['B', 'D', 'F'],
    }

    conti = 2

    while 1:
        queue = ['Am', 'G', 'F', 'C']
        for j in queue:
            for __ in range(2):
                for _ in range(conti):
                    for i in chordsToNotes[j]:
                        playsound(f'chordWavs/singleNotes/{i}.wav', False)
                        time.sleep(speed)

                playsound(f'chordWavs/singleNotes/{chordsToNotes[j][0]}.wav', False)
                time.sleep(speed)
                playsound(f'chordWavs/singleNotes/{chordsToNotes[j][2]}.wav', False)
                time.sleep(speed)

def readInput():
    global speed
    pygame.midi.init()
    input_device=pygame.midi.Input(0)
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            print (number_to_note(note_number), velocity,note_number)
            if note_number==21:
                speed=velocity/100

if __name__ == '__main__':
    Thread(target=notes).start()
    # Thread(target=update).start()
    Thread(target=readInput).start()
