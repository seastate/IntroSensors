# snoozeLED.py: An example of Pulse Width Modulation, used to snooze an LED.
#
# Default settings, and their alternatives:
#        -- use GPIO 2, the blue on-board LED  (0, 2, 4, 5, 12, 13, 14 and 15 support PWM)
#        -- 1000 cycles per second (1-1000 Hz valid range)
#        -- 200 duty cycle (valid range is 1023 (full on) to 0 (full off) 

def snooze_led(pin=2,freq=1000,delta=50,delay=150,verbose=False):
    from machine import Pin, PWM  # import the necessary modules
    from time import sleep_ms     # to define pins and sleep
    pwm = PWM(Pin(pin))      # create PWM object from a pin
    pwm.freq(freq)             # get current frequency

    duty=0
    while True:         # Start a loop that runs forever
        if duty<=0:     # change sign of adjustment of duty cycle
            delta_=delta
            duty=0
        elif duty>=1000:
            delta_=-delta
            duty=1000
        duty += delta_     # adjust duty cycle
        pwm.duty(duty)  # apply the duty cycle to the PWM pin
        if verbose:
            print(pwm)
        sleep_ms(delay)    # short pause between adjustments
