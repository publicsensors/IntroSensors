from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import os, glob

def parse_tsl237_divider(filename):
    """ A function to parse light sensor frequency data from
        a file generated by light_freq.py"""
    # Initialize lists to hold data from file being parsed
    avg_ts=[]
    avg_ds=[]
    ratio_d_ts=[]
    freq_ts=[]
    freq_ds=[]
    with open(filename,'r') as file:
        counter=0
        for line in file:
            data=line.split('\t') # We use tab as a delimiter
            #data=line.split(' ') # We use a space as a delimiter
            # The first number is the sample number. Subsequent numbers are day, hour, minute, second
            # for each of onboard RTC, external RTC and NTP server.
            #series_num=int(data[0]) 
            avg_ts.append(float(data[0]))
            avg_ds.append(float(data[1]))
            ratio_d_ts.append(float(data[2]))
            freq_ts.append(float(data[3]))
            freq_ds.append(float(data[4]))

            counter+=1            
    print('parsed ',counter,' data lines...')
    return avg_ts,avg_ds,ratio_d_ts,freq_ts,freq_ds

def plot_tsl237_divider(filename,timeout=None,min_per=None):
    """ A function to parse light sensor frequency data from
        a file generated by light_freq.py"""
    avg_ts,avg_ds,ratio_d_ts,freq_ts,freq_ds=parse_tsl237_divider(filename)
    
    plt.figure()
    plt.plot([1e0,1e6],[1e-1,1e5],color='k',linestyle=':')
    if timeout is not None:
        plt.axvline(timeout,color='r',linestyle=':')
        plt.axhline(timeout,color='r',linestyle=':')
    if min_per is not None:
        plt.axvline(min_per,color='b',linestyle=':')
        plt.axhline(min_per,color='b',linestyle=':')
    plt.annotate('1:10 line',xy=(3e4,1.5e3), xycoords='data')
    plt.annotate('timeout',xy=(timeout/7,timeout/3), xycoords='data',color='r')
    plt.annotate('min. per.',xy=(min_per/7,min_per/3), xycoords='data',color='b')
    
    plt.plot(avg_ds,avg_ts,'.')
    plt.xlabel('Divider period ($\mu s$)')
    plt.ylabel('TSL237 period ($\mu s$)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Period comparison: TSL237 vs. divider')
    plt.grid(True)

    plt.show()
