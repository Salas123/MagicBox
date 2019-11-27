import pygame
import os
import time

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.mouse.set_visible(False)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render('Temperature:', True, (255,255,255))
textRect = text.get_rect()

while True:
	lcd.fill((255,0,0))
	lcd.blit(text,textRect)
	pygame.display.update()
	time.sleep(1)
