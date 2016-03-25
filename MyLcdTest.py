#!/usr/bin/python
# Import Modules for project.
import time
import Adafruit_CharLCD as LCD

# Raspberry Pi LCD pin configuration:

lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 27
lcd_d7        = 22
lcd_backlight = 25

# Define column and row size 20x4 LCD.
lcd_columns = 20
lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
lcd_columns, lcd_rows, lcd_backlight)

# Scrolling message right/left.
lcd.clear()
message = 'Dale Cooper'
lcd.message(message)
for i in range(lcd_columns-len(message)):
	time.sleep(0.5)
	lcd.move_right()
for i in range(lcd_columns-len(message)):
	time.sleep(0.5)
	lcd.move_left()
time.sleep(5)
lcd.clear()
lcd.message('Goodbye :-)')
time.sleep(5)
