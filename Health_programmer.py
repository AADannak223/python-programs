
import time
from pygame import mixer

initial = (time.localtime(time.time()))
# print(initial[4])

if (initial[3] == 9) and (initial[4] == 0) and (initial[5] == 0):

    while True:
        initial1 = (time.localtime(time.time()))
        a = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        i = 0

        if (initial[3] == a[i]) and (initial[4] == 0) and (initial[5] == 0):
            # Starting the mixer
            mixer.init()

            # Loading the song
            mixer.music.load("Water.mp3")

            # Setting the volume
            mixer.music.set_volume(1)

            # Start playing the song
            mixer.music.play()

            print("Press 'Drank' to pause")
            query = input("  ")

            if query == 'Drank':
                # Pausing the music
                mixer.music.pause()
        break










