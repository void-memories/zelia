import time
import pygame
import pygame.midi
from playsound import playsound
from threading import Thread
import mido
import random


speed = 1
notesQueue = []
play=0
chord_arp=0
maj_min=1
loop_1s=1


def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number % 12]


def chords():
    pygame.mixer.init()

    global speed
    global notesQueue
    queue = notesQueue
    while 1:
        index = 0
        for i in queue:
            if play==0 or chord_arp==1:
                return
            playsound(f'chordWavs/90BPM/{i}.wav', False)
            time.sleep(speed)

            index += 1


def notes():
    global speed
    global notesQueue
    queue = notesQueue
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

        while 1:
            j = random.choice(queue)
            for __ in range(2):
                for _ in range(conti):
                    index = 0
                    for i in chordsToNotes[j]:
                        if play==0 or chord_arp==0:
                            return
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


def readInput():
    global speed
    global notesQueue
    global play
    global chord_arp
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

            if note_number == 51:
                play^=1
                if play==1:
                    if chord_arp==0:
                        Thread(target=chords).start()
                    else:
                        Thread(target=notes).start()
                    

            elif note_number == 52:
                chord_arp ^= 1
                if play==1:
                    if chord_arp==0:
                        Thread(target=chords).start()
                    else:
                        Thread(target=notes).start()
            elif note_number == 53:
                maj_min ^= 1
            elif note_number == 54:
                loop_1s ^= 1
            elif note_number == 55:
                speed = 0.635-(velocity/1000)*5
                print(speed)
            elif note_number > 55:
                selection = note_number-55
                if selection == 1:
                    notesQueue.append('C')
                elif selection == 2:
                    notesQueue.append('Dm')
                elif selection == 3:
                    notesQueue.append('Em')
                elif selection == 4:
                    notesQueue.append('F')
                elif selection == 5:
                    notesQueue.append('G')
                elif selection == 6:
                    notesQueue.append('Am')
                elif selection == 7:
                    notesQueue.append('B')
                elif selection == 8:
                    try:
                        fff=notesQueue.pop()
                    except:
                        do = 1


if __name__ == '__main__':

    Thread(target=readInput).start()
