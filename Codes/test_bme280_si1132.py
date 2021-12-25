# test_bme280_si1132.py
# Example combining I2C and SMBus devices on a single bus.
#
# Modify pin numbers to reflect your circuit layout.
# Replace bme280_float with bme280_int if your
# microcontroller does not support floating point math.
#
from machine import I2C, Pin
from bme280_float import *
from si1132 import SI1132 
from utime import sleep
from usmbus import SMBus

# Initialize the I2C bus
i2c = I2C(scl=Pin(5, Pin.IN),sda=Pin(4, Pin.IN))
# Initialize the SMBus on the same pins
bus = SMBus(scl=Pin(5, Pin.IN),sda=Pin(4, Pin.IN))
# Create BME280 and SI1132 objects
bme280 = BME280(i2c=i2c)
si1132 = SI1132(smbus=bus)
#
while True:
    print('\nbme280: ',bme280.values)
    uv, ir, visible = si1132.read()
    sleep(1)
