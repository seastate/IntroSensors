"""Example Code for MH-Z14A CO2 sensor
Wes Lauer
January 8, 2022
Released under MIT license

This program uses a serial UART connect to read data from a
MH-Z14A or MH-Z19B carbon dioxide sensor.
"""

import time
import machine
from machine import Pin

ser = machine.UART(1,baudrate=9600, rx=38, tx=39)  #RX & TX for Adafruit ESP32-S2 Feather-S2
ser.init(9600, bits=8, parity=None, stop=1)

BuiltinLED = Pin(13, Pin.OUT) #for Adafruit ESP32-S2 Feather-S2
BuiltinLED.on()

#define codes
code_read = b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79'
code_calibrate = b'\xFF\x01\x87\x00\x00\x00\x00\x00\x78'

#if calibration is desired, execute the following after sensor has been sitting in outdoor air for 20 minutes
#ser.write(code_calibrate)

#take a reading
ser.readline()
written = ser.write(code_read) #assign the result to a variable so it won't print to screen
time.sleep(1)
response = ser.readline()
print('acknowledgement is:')
print(response)
co2 = 256*response[2]+response[3]
print('CO2 = %s' % (co2))

#enter read loop
while True:
    ser.readline()
    written = ser.write(code_read) #assign the result to a variable so it won't print to screen
    time.sleep(5)
    try:
        response = ser.readline()
        co2 = 256*response[2]+response[3]
        print('CO2 = %s' % (co2))
    except:
        pass



