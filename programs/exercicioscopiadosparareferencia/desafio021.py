###import playsound
###playsound.playsound('ex021.mp3')

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
import time
time.sleep(360)
