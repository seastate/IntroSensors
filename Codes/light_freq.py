from machine import Pin
from time import sleep
import sys
#
#  This code is based on the original post by RobertHH at
#  https://forum.micropython.org/viewtopic.php?f=18&t=5724&p=32921
#  Modified by D. Grunbaum on 2020-02-23 to handle timeout errors
#  and optionally provide verbose output. 
#  Both original and this modification are released under the MIT
#  license (https://opensource.org/licenses/MIT)
#
from frequency_median import median_of_n

def compare_tsl237_divider(p_tsl237=4,p_div=5,timeout=300000, \
                           nrep=7,navg=8,divide=10.,verbose=False):
    # Makes successive measurements of frequency,
    # directly from a TSL237 light sensor on pin p_tsl237
    # and through a 10x frequency divider on pin p_div.    
    assert (0<timeout<1000000), 'require 0 < timeout <= 1000000'

    pt = Pin(p_tsl237, Pin.IN) # create pin objects
    pd = Pin(p_div, Pin.IN)
    
    avg_t = 0
    avg_d = 0
    for avg in range(navg):
        try:
            per_d,status_d=median_of_n(pd,nrep,timeout,verbose=False)
            per_t,status_t=median_of_n(pt,nrep,timeout,verbose=False)
            avg_t += per_t
            avg_d += per_d
            if verbose:
                print(per_t," \t  ",per_d," \t  ",status_t," \t  ",status_d)
        except Exception as ex:
            print('error in frequency measurement, ',ex)
    avg_t/=float(navg)
    avg_d/=float(navg)
    print(avg_t," \t  ",avg_d," \t  ",avg_d/avg_t," \t  ",1000000/avg_t," \t",divide*1000000./avg_d)
    sleep(0.1)
    return [avg_t,avg_d,avg_d/avg_t,1000000/avg_t,divide*1000000./avg_d]

def file_exists(filename):
    from os import stat
    try:
        stat_=stat(filename)
        return True
    except:
        return False

def record_tsl237_divider(p_tsl237=4,p_div=5,timeout=300000, \
                           nrep=7,navg=8,divide=10.,nsample=5,verbose=False, \
                          filename='tsl237_divider.dat'):
    # Records successive measurements of frequency,
    # directly from a TSL237 light sensor on pin p_tsl237
    # and through a frequency divider.    


    
    if file_exists(filename):
        print("File exists: enter: o=overwrite; a=append; e=exit")
        reply=sys.stdin.read(2)[1]
        #reply = str(raw_input("File exists: enter: o=overwrite; a=append; e=exit")).lower().strip()
        if reply[:1] == 'o':
            print("opening new file...")
            datafile=open(filename,'w')  # If the first sample, overwrite old tmp_file if it exists
        elif reply[:1] == 'a':
            print("appending to existing file...")
            datafile=open(filename,'a')  # Otherwise, append new data to existing file 
        else:
            print("exiting...")
            return 
    else:
        print("opening new file...")
        datafile=open(filename,'w')  # If the first sample, overwrite old tmp_file if it exists

    while True:
        data=[]
        for smpl in range(nsample):
            data.append(compare_tsl237_divider(p_tsl237=p_tsl237,p_div=p_div,timeout=timeout, \
                               nrep=nrep,navg=navg,divide=divide,verbose=verbose))
        print("Save data to file? y=yes; n=no; e=exit")
        reply = sys.stdin.read(1)
        #reply = str(raw_input("Save data to file? y=yes; n=no; e=exit")).lower().strip()
        if reply[:1] == 'y':
            print("saving data...")
            for d in data:
                datafile.write("\t".join( map(str, d) )+"\n" )
        elif reply[:1] == 'e':
            datafile.close()
            print("exiting...")
            return
        else:
            print("discarding data...")
        



            




        
