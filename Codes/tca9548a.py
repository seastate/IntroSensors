import machine
import ustruct

scl_pin=5
sda_pin=4

class TCA9548A():
    def __init__(self,address):
        self.address=address
        self.bus=machine.I2C(machine.Pin(scl_pin), machine.Pin(sda_pin))
        #self.bus=machine.I2C(-1, machine.Pin(scl_pin), machine.Pin(sda_pin))

    def switch_channel(self,channel):
        self.bus.writeto(self.address,ustruct.pack('B',1 << channel))

