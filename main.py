import time
import pygame
import pygame.midi
from playsound import playsound
from threading import Thread
import mido
import random


speed = 1


def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number % 12]


def update():
    global speed
    while 1:
        speed = float(input('new tempo '))


def chords():
    pygame.mixer.init()

    global speed
    queue = ['F', 'Am', 'C', 'G']
    while 1:
        index = 0
        for i in queue:
            color = random_color()
            playsound(f'chordWavs/90BPM/{i}.wav', False)
            time.sleep(speed)

            index += 1

            # pygame.mixer.Sound(f'chordWavs/90BPM/{i}.wav').play()
            # pygame.mixer.music.play()

            # time.sleep(2.5)
            # 2==120BPM
            # 2.5==90BPM


def notes():
    global speed
    pygame.midi.init()
    player = pygame.midi.Output(1)
    player.set_instrument(0)

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
        queue = ['Am', 'B', 'C', 'Dm', 'Em', 'F', 'G']
        while 1:
            j = random.choice(queue)
            for __ in range(2):
                for _ in range(conti):
                    index = 0
                    for i in chordsToNotes[j]:
                        playsound(f'chordWavs/singleNotes/{i}.wav', False)
                        player.note_on(44, 8+index)
                        time.sleep(speed)
                        player.note_off(44, 8+index)
                        index += 1

                playsound(f'chordWavs/singleNotes/{chordsToNotes[j][0]}.wav', False)
                player.note_on(44, 8)
                time.sleep(speed)
                player.note_off(44, 8)
                playsound(f'chordWavs/singleNotes/{chordsToNotes[j][2]}.wav', False)
                player.note_on(44, 10)
                time.sleep(speed)
                player.note_off(44, 10)

                # pygame.mixer.Sound(f'chordWavs/singleNotes/{i}.wav').play()
                #         time.sleep(speed)

                # pygame.mixer.Sound(f'chordWavs/singleNotes/{chordsToNotes[j][0]}.wav').play()
                # time.sleep(speed)
                # pygame.mixer.Sound(f'chordWavs/singleNotes/{chordsToNotes[j][2]}.wav').play()
                # time.sleep(speed)


def readInput():
    global speed
    pygame.midi.init()
    input_device = pygame.midi.Input(0)
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]
            print (number_to_note(note_number), velocity, note_number)
            if note_number == 16:
                speed = velocity/100


if __name__ == '__main__':
    # midi_out = mido.open_output("Launchkey Mini LK Mini InControl")
    # midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))
    # midi_out.send(mido.Message('note_on', channel=0, note=8, velocity=1))

    Thread(target=notes).start()
    # Thread(target=update).start()
    Thread(target=readInput).start()
