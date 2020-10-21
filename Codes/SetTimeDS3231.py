def settimeDS3231(sclPin=5, sdaPin=4):
    from ntptime import time # use the ntp method provided in firmware
    import urtc
    from machine import I2C, Pin
    import utime
    t = time()
    tm = utime.localtime(t)
    i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin))
    rtc_ds3231 = urtc.DS3231(i2c)
    datetime = urtc.datetime_tuple(year=tm[0], month=tm[1], day=tm[2],hour=tm[3],minute=tm[4],second=tm[5])
    print('setting urtc datetime to: ',datetime)
    rtc_ds3231.datetime(datetime)
    datetime = rtc_ds3231.datetime()
    print('verifying: rtc_ds3231.datetime() = ',datetime)

