# coding=UTF-8
# !/usr/bin/env python
# ----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7.
#		replace the 28-XXXXXXXXX as yours.
# ----------------------------------------------------------------
import os, time, datetime, ftplib

ds18b20 = '28-21607ec4dcff'


def setup():
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i


def read():
    #	global ds18b20
    try:
        location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        # print(text)
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature
    except:
        print("温度传感器异常")
        return 0


def readTemp():
    setup()
    return read()


if __name__ == '__main__':
    # try:
    # setup()
    # while True:
    #     print(read())
    print(readTemp(ds18b20))
# except:
# 	print("program error!")
