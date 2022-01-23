"""Example Code for Honeywell HPMA1115S0-XXX particulate sensor
Wes Lauer
January 8, 2022
Released under MIT license

This program uses a serial UART connect to read data from a
Honeywell HPMA1115S0 PM2.5/PM10 sensor.
"""
import machine
from machine import Pin
import time    #for pausing and looping

ser = machine.UART(1,baudrate=9600, rx=38, tx=39)  #RX & TX for Adafruit ESP32-S2 Feather-S2
BuiltinLED = Pin(13, Pin.OUT)
BuiltinLED.on()

#define codes
code_stop_auto_send = b'\x68\x01\x20\x77'
code_stop = b'\x68\x01\x02\x95'
code_start = b'\x68\x01\x01\x96'
code_read = b'\x68\x01\x04\x93'

#stop auto send function--this makes learning UART less confusing because results don't keep stacking up in the queue
ser.readline()
ser.write(code_stop_auto_send)
time.sleep(1)
response = ser.readline()
print('command sent, acknowledgement is:')
print(response)

#turn reading off -- confirm that this stopped fan
ser.readline()
ser.write(code_stop)
time.sleep(0.5)
response = ser.readline()
print('command sent, acknowledgement is:')
print(response)

#turn reading on -- confirm that this started fan
ser.readline()
ser.write(code_start)
time.sleep(0.5)
response = ser.readline()
print('acknowledgement is:')
print(response)

#read particulate results -- 68 01 04 93
ser.readline()
ser.write(code_read)
time.sleep(1)
response = ser.readline()
print('started, acknowledgement is:')
PM25 = response[3]*256+response[4]
print('PM2.5 = ');
print(PM25)
PM10 = response[5]*256+response[6]

#enter read loop
while True:
    written = ser.write(code_read) #assign the result to a variable so it won't print to screen
    time.sleep(6)  #data sheet says response time is under 6 seconds
    response = ser.readline()
    if response[0] == 64 and len(response)==8:
        PM25 = response[3]*256+response[4]
        PM10 = response[5]*256+response[6]
        print('PM2.5 = %s; PM10 = %s' % (PM25, PM10))
    else:
        time.sleep(10)
        response = ser.readline()