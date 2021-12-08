
# Import driver for multiplexer
from tsc9548a import TCA9548A
# Import driver for color sensor
from tcs34725 import TCS34725
# Import driver for light sensor
from tsl2591 import Tsl2591

tca=TCA9548A(0x70)

color_channel=1
light_channel=0

# Initialize light sensor
tca.switch_channel(light_channel)
light_sensor = Tsl2591(tca.bus)

# Initialize color sensor
tca.switch_channel(color_channel)
color_sensor = TCS34725(tca.bus)

for i in range(10):
    # Sample using light sensor
    tca.switch_channel(light_channel)
    light_sample = light_sensor.sample()
    print('light_sample = ',light_sample)

    # Sample using color sensor
    tca.switch_channel(color_channel)
    color_sample = color_sensor.read(True)
    print('color_sample = ',color_sample)