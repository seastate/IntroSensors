# SteinhartHart.py: Calculation for the Steinhart-Hart
#                   equations, calibrating thermistor
#                   resistance as a function of temperature.
#
from math import log # import the natural log function

def SH_coeffs_kelvin(T1k=273.15,R1=32648.,T2k=298.15,R2=9999.,T3k=373.15,R3=680.):
    try:
        L1=log(R1)
        L2=log(R2)
        L3=log(R3)
        Y1=1./T1k
        Y2=1./T2k
        Y3=1./T3k
        gamma2=(Y2-Y1)/(L2-L1)
        gamma3=(Y3-Y1)/(L3-L1)
        # Calculate the Steinhart-Hart coefficients
        C=(gamma3-gamma2)/(L3-L2)*(L1+L2+L3)**(-1)
        B=gamma2-C*(L1**2+L1*L2+L2**2)
        A=Y1-(B+L1**2*C)*L1
        return (A,B,C)
        
    except:
        print('Error in calculating Steinhart-Hart coefficients. Use SH_coeffs_celsius if temperature is in Celsius.')

def SH_coeffs_celsius(T1c=0.,R1=32648.,T2c=25.,R2=9999.,T3c=100.,R3=680.):
    """Calculate the Steinhart-Hart coefficients, with input temperatures in Celsius"""

    return SH_coeffs_kelvin(T1k=T1c+273.15,R1=R1,T2k=T2c+273.15,R2=R2,T3k=T3c+273.15,R3=R3)

