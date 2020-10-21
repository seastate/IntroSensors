from machine import ADC   # import the ADC module
def battery_voltage(R1=470.,R2=47.):
    adc=ADC(0)             # create an ADC object
    vdata=adc.read()/1024. # read the ADC, calculate vdata
    vin=(R1+R2)/R2*vdata   # calculate vin from vdata
    return vin
