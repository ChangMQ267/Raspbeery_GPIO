# /usr/bin/python3
import spidev
import time
import os
import csv

# TDS 计算  66.71 * data * data * data - 127.93 * data * data + 428.7 * data

def readadc(channel):
    value = spi.xfer2([1, (8 + channel) << 4, 0])
    read = ((value[1] & 3 << 8) + value[2])
    return read


spi = spidev.SpiDev()
spi.open(0, 0)
# writer = csv.writer(filter('Datalog.csv','ab+'))
while True:
    datalist = []
    # for i in range(0, 8):
    data = readadc(0)
    print(data)
    datalist.append(data)
    temp = 66.71 * data * data * data - 127.93 * data * data + 428.7 * data
    print(temp)
    time.sleep(3)
print(datalist)
# writer.writerow(datalist)
