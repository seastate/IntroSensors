from machine import time_pulse_us
#  This code is based on the original post by RobertHH at
#  https://forum.micropython.org/viewtopic.php?f=18&t=5724&p=32921
#  Modified by D. Grunbaum on 2020-02-23 to handle timeout errors
#  and optionally provide verbose output. 
#  Both original and this modification are released under the MIT
#  license (https://opensource.org/licenses/MIT)
def median_of_n(p, n, timeout,verbose=False):
    # Return the median of n frequency measurements
    # on pin p, using time_pulse_us with timeout
    set = []
    for i in range(n):
        try:
            v0=time_pulse_us(p, 1, timeout)
            if v0<0:
                return timeout,False
            v1 = time_pulse_us(p, 1, timeout)
            if v1<0:
                return timeout,False
            v2=time_pulse_us(p, 0, timeout)
            if v2<0:
                return timeout,False
            v3 = time_pulse_us(p, 0, timeout)
            if v3<0:
                return timeout,False
            set.append(v1+v3)
        except Exception as ex:
            print('exception =',ex, ' on sample ',i)
    set.sort()
    if verbose:
        print(set[n//2],set)
    return set[n//2],True
