# thermistor.py:  Calculations using the Steinhart-Hart equations to calculate
#                         thermistor temperature from resistance, and vice versa.

from math import log,sqrt,exp # import math functions

def thermistor_temp_kelvins(Rth=0.,A=0.,B=0.,C=0.):
    """Calculate thermistor temperature in kelvins as a function of resistance, 
        given its Steinhart-Hart coefficients."""
    lnRth=log(Rth)
    Tk=(A+B*lnRth+C*lnRth**3)**(-1)
    return Tk

def thermistor_temp_celsius(Rth=0.,A=0.,B=0.,C=0.):
    Tk=thermistor_temp_kelvins(Rth=Rth,A=A,B=B,C=C)
    Tc=Tk-273.15
    return Tc
            
def thermistor_res_kelvins(Tk=0.,A=0.,B=0.,C=0.):
    """Calculate thermistor resistance  as a function of temperature in kelvins, 
        given its Steinhart-Hart coefficients."""
    # Calculate the inverse Steinhart-Hart coefficients.
    x=1./(2.*C)*(A-1./Tk)
    y=sqrt((B/(3.*C))**3+x**2)
    Rth=exp((y-x)**(1./3.)-(y+x)**(1./3.))
    return Rth

def thermistor_res_celsius(Tc=0.,A=0.,B=0.,C=0.):
    """Calculate thermistor resistance  as a function of temperature in Celsius, 
        given its Steinhart-Hart coefficients."""
    Rth=thermistor_res_kelvins(Tk=Tc+273.15,A=A,B=B,C=C)
    return Rth
