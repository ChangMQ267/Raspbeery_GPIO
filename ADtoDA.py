# /usr/bin/python3
import spidev
import time
import os
import csv


def readadc(channel):
    value = spi.xfer2([1, (8 + channel) << 4, 0])
    read = ((value[1] & 3 << 8) + value[2])
    return read


spi = spidev.SpiDev()
spi.open(0, 0)
# writer = csv.writer(filter('Datalog.csv','ab+'))
while True:
    datalist = []
    for i in range(0, 8):
        data = readadc(i)
        print(data)
        datalist.append(data)
        temp = ((data * 330) / float(1023)) - 50
        print(temp)
        time.sleep(3)
    print(datalist)
    # writer.writerow(datalist)
