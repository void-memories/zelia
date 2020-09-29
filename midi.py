import pygame
import pygame.midi
import time
from playsound import playsound


def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number % 12]


def chords():
    pygame.mixer.init()
    queue = ['F', 'Am', 'C', 'G']
    while 1:
        for i in queue:
            toPlay = pygame.mixer.Sound(f'chordWavs/90BPM/{i}.wav')
            pygame.mixer.Sound.play(toPlay)
            time.sleep(1)
        break


def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            # print(event)
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            print (number_to_note(note_number), velocity, note_number)
            if note_number == 50:
                chords()


pygame.midi.init()
mi = pygame.midi.Input(0)
readInput(mi)
