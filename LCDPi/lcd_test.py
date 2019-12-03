import pygame
import os
import time
import board
import busio
import adafruit_bme280
import datetime

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.mouse.set_visible(False)
pygame.font.init()

#temperature text
font_temp = pygame.font.Font('freesansbold.ttf', 30)
text_temp = font_temp.render('Temperature:', True, (255,255,255))
texttemp_Rect = text_temp.get_rect(center=(160,140))

#time text
font_time = pygame.font.Font('freesansbold.ttf', 30)
text_time = font_time.render('Time:', True, (255,255,255))
texttime_Rect = text_time.get_rect(center=(160,50))

counter = 0

while counter <= 3:

		newTempVal = (bme280.temperature * (9/5)) + 32
		strTempVal = str(round(newTempVal)) + "F"
		#actual temperature value
		font_tempVal = pygame.font.Font('freesansbold.ttf', 30)
		text_tempVal = font_tempVal.render(strTempVal,True,(255,255,255))
		texttempVal_Rect = text_tempVal.get_rect(center=(150,190))

		font_timeVal = pygame.font.Font('freesansbold.ttf', 30)
		text_timeVal = font_timeVal.render(time.strftime("%r"),True,(255,255,255))
		texttimeVal_Rect = text_timeVal.get_rect(center=(160, 90))


		lcd.fill((51,153,255))
		lcd.blit(text_temp,texttemp_Rect)
		lcd.blit(text_time,texttime_Rect)
		lcd.blit(text_tempVal,texttempVal_Rect)
		lcd.blit(text_timeVal,texttimeVal_Rect)
		pygame.display.update()
		time.sleep(1)
		counter += 1
