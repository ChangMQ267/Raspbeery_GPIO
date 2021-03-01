# /usr/bin/python3
import spidev
import time
import Temperature as temp
import os

# init()
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 15600000
MAXNUM = 0


def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    print("adc:", str(adc))
    readdata = ((adc[1] & 3) << 8) + adc[2]

    return readdata


def ConvertTDS(readdata, Temp):
    Temp_value = 1 + 0.02 * (Temp - 25)
    data_value = Temp_value * readdata
    tds_value = 66.71 * data_value * data_value * data_value - 127.93 * data_value * data_value + 428.7 * data_value
    return tds_value


num = 0

while True:
    # for i in range(0, 8):
    print(num, str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    data = ReadChannel(0)
    print("data:", data)
    datatrue = data * (3.3 / float(1023))
    if data > MAXNUM:
        MAXNUM = data
    print("readdata:", datatrue)
    Temp = temp.readTemp()
    print("Temp:", Temp)
    tds = ConvertTDS(datatrue, Temp)
    print("tds:", tds)
    time.sleep(2)
    print(MAXNUM)
