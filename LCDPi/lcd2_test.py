import pygame
import time
import os

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.mouse.set_visible(False)
pygame.font.init()

#temperature text
font_temp = pygame.font.Font('freesansbold.ttf', 30)
text_temp = font_temp.render('Project:', True, (255,255,255))
texttemp_Rect = text_temp.get_rect(center=(150,80))

counter = 0

while counter <= 3:

                font_tempVal = pygame.font.Font('freesansbold.ttf', 55)
                text_tempVal = font_tempVal.render('Magic Box',True,(255,255,255))
                texttempVal_Rect = text_tempVal.get_rect(center=(160,155))

                lcd.fill((255,192,203))
                lcd.blit(text_temp,texttemp_Rect)
                lcd.blit(text_tempVal,texttempVal_Rect)
                pygame.display.update()
                time.sleep(1)
                counter+=3



