#  TimeCompare.py
#  Example code to create a dataset, to assess accuracy and precision
#  of on-board and external RTCs relative to an NTP server.
# 
from machine import RTC, unique_id
import urtc
import ntptimeDS3231
import utime
from machine import I2C, Pin
from network import WLAN, STA_IF
from ubinascii import hexlify
from os import rename
from gc import collect
collect()      # Free up heap space 

"""
#  An example of a typical execution sequence:
from TimeCompare import time_compare

# Initialize on-board RTC
rtc_ = RTC()

# Initialize DS3231 (external) RTC
i2c = I2C(scl=Pin(5), sda=Pin(4))
rtc3231_=urtc.DS3231(i2c)

#---------------------------------------
# Sampling parameters
#---------------------------------------
prefix_='danny'

interval_seconds=10        #  Sampling interval, in seconds
#interval_seconds=1*60     #  A format making it easy to specify intervals in minutes
#interval_seconds=1*60*60     #  A format making it easy to specify intervals in hours

num_samples= 10      # Number of time intervals to sample
num_replicates = 3   # Number of times to replicate the sampling protocol

time_compare(prefix=prefix_,rtc=rtc_,rtc3231=rtc3231_,interval_seconds=20,num_samples=10,num_replicates=4)

"""

def time_compare(prefix='danny',rtc=None,rtc3231=None,interval_seconds=20,num_samples=10,num_replicates=8):
    """ Run comparisons of the on-board and external RTC's to assess relative accuracy and precision. 

        To execute successfully, rtc_ and rtc3231_ should be declared outside the function and supplied as arguments.
        Other parameters may be modified or left as defaults.
    """
    print('\nUsing sampling interval ',interval_seconds,' seconds...')
    print('Collecting ',num_replicates,' replicates of ',num_samples,' samples...\n')
    ID=hexlify(unique_id()).decode('utf-8') # Unique ID of the microprocessor
    tmp_file='tmp.txt'  # A temporary filename; we will write partial data to this file, and rename only if sampling succeeds

    #---------------------------------------
    # Loop over all the replicates:
    #---------------------------------------
    for i_rep in range(num_replicates):
        print('\n\n****Beginning replicate ',i_rep,' ****\n\n')

        #---------------------------------------
        #  Initialize clocks: the DS3231 is set (if possible) from the NTP server; the on-board RTC is then set from the DS3231
        #---------------------------------------
        print("\nTrying to set the DS3231 RTC using NTP...")
        try:
            ntptimeDS3231.settimeDS3231()
            print('...successfully set from NTP') 
        except: # execute the following if the previous section triggerd an error (usually because not connected to the internet)
            print('...unable to set from NTP') 

        # Set the on-board RTC from the external RTC:
        dt3231=rtc3231.datetime()
        rtc.datetime((dt3231.year,dt3231.month,dt3231.day,0,dt3231.hour,dt3231.minute,dt3231.second,0))

        #print('\nThese two should match:')
        #rtc.datetime()  # print out current onboard RTC date/time tuple
        #datetime = rtc3231.datetime()
        #print(datetime)  # print out current DS3231 date/time tuple

        # Initialize file name using current timestamp;
        timestamp=str(utime.mktime(rtc.datetime()))
        filename=prefix+'_'+ID+'_'+timestamp+'.txt'
        print('\nCreating data file: ',filename)

        #---------------------------------------
        # Loop through comparisons of RTC and NTP values
        #---------------------------------------
        print('\n\nsample_num,day_onboard,hour_onboard,min_onboard,sec_onboard,day_external,hour_external,min_external,sec_external,day_NTP,hour_NTP,min_NTP,sec_NTP')
        for sample_num in range(num_samples+1):
            t_onboard=rtc.datetime()  # print out current date/time tuple
            t_external=rtc3231.datetime()  # print out current date/time tuple
            try:
                tNTP=utime.localtime(ntptimeDS3231.time())
                tNTPmday=tNTP[2]
                tNTPhour=tNTP[3]
                tNTPminute=tNTP[4]
                tNTPsecond=tNTP[5]
            except:
                tNTPmday=-1
                tNTPhour=-1
                tNTPminute=-1
                tNTPsecond=-1

            data_str=''
            for t in [sample_num,t_onboard[2],t_onboard[4],t_onboard[5],t_onboard[6],t_external.day,t_external.hour, \
                          t_external.minute,t_external.second,tNTPmday,tNTPhour,tNTPminute,tNTPsecond]:
                data_str+='{} '.format(t)
            print(data_str)

            # Write data to file. Use a temporary filename that will be overwritten if sampling is interupted
            if sample_num==0:
                datafile=open(tmp_file,'w')  # If the first sample, overwrite old tmp_file if it exists
            else:
                datafile=open(tmp_file,'a')  # Otherwise, append new data to existing file 
            df=datafile.write("%s\n" % data_str) # df contains the "result" of the write statement (success or failure)
            datafile.close()

            #print(sample_num,t_onboard[5],t_onboard[6],t_external.minute,t_external.second)
            if sample_num<num_samples:  # Sleep only if another sample is to be taken
                utime.sleep(interval_seconds)

        #---------------------------------------
        # Done with the comparison loop; change the temporary filename to the permanent one, now that sampling is complete
        #---------------------------------------
        rename(tmp_file,filename)
