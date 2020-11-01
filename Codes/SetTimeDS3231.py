def settimeDS3231(sclPin=5, sdaPin=4):
    """Code to set a DS3231 external Real Time Clock from an NTP server
    """
    from ntptime import time # use the ntp method in firmware
    import urtc
    from machine import I2C, Pin
    import utime
    t_ntp = time()   # get time from the NTP server
    tm_ntp = utime.localtime(t_ntp)  # convert time format
    # initialize I2C interface & create I2C device for clock
    i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin)) 
    rtc_ds3231 = urtc.DS3231(i2c)
    # get time from the DS3231
    datetime_ds3231 = rtc_ds3231.datetime() 
    print('Before resetting: rtc_ds3231.datetime() = ',datetime_ds3231)
    new_datetime = urtc.datetime_tuple(year=tm[0], month=tm[1], day=tm[2],hour=tm[3],minute=tm[4],second=tm[5])
    print('setting DS3231 datetime from NTP to: ',new_datetime)
    rtc_ds3231.datetime(new_datetime)  # Set new ds3231 time
    # confirm new time was set on ds3231
    datetime_ds3231 = rtc_ds3231.datetime() 
    print('After resetting: rtc_ds3231.datetime() = ',datetime_ds3231)

