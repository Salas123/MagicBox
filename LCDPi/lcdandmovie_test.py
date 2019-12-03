import os
import time

def runMovie(timeForSleep):
	os.system('sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop dballz.mp4')
	time.sleep(timeForSleep)

def runTempScreen(timeForSleep):
	os.system('sudo python3 lcd_test.py')
	time.sleep(timeForSleep)
	os.system('sudo python3 lcd2_test.py')

while True:
	try:
		runMovie(0.5)
		runTempScreen(0.5)

	except KeyboardInterrupt:
		exit()



