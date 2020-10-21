# button_interrupt.py: An example of using an interrupt to trigger a response.
from machine import Pin 
# Define GPIO 0 as an output, to be set by the handler:
pin0 = Pin(0, Pin.OUT)                   
# Define GPIO 2 as an input, responding to a button push:
pin2 = Pin(2, Pin.IN,pull=Pin.PULL_UP)   

# Define a handler to toggle Pin 0
def togglePin0(arg):    
    if pin0.value()==0: # If low, set pin high
        pin0.value(1)
    else:               # if high, set pin low
        pin0.value(0)
    print('GPIO 0 set to ',pin0.value())
    
# Program GPIO 2 to call the handler each time the button is depressed
pin2.irq(handler=togglePin0,trigger=Pin.IRQ_FALLING)
# Program GPIO 2 to call the handler each time the button is released
#pin2.irq(handler=togglePin0,trigger=Pin.IRQ_RISING)
# Program GPIO 2 to call the handler each time the button is depressed or released
#pin2.irq(handler=togglePin0,trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING)
