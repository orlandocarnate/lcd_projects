import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello, Orlando!",1)
mylcd.lcd_display_string("This is a test.",2)
