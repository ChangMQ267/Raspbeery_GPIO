# /usr/bin/python3
import spidev
import time
import Temperature as temp
import os

# init()
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 15600000

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    print("adc:", str(adc))
    readData = ((adc[1] & 3) << 8) + adc[2]

    return readData


def ConvertTDS(voltage, temperature):
    temperature = 1 + 0.02 * (temperature - 25)

    # tds_value = 133.42 * voltage * voltage * voltage - 255.86 * voltage * voltage + 857.39 * voltage
    # tds_value = tds_value / (1.0 + 0.02 * (temperature - 25.0));

    voltage = temperature * voltage
    tds_value = 66.71 * voltage * voltage * voltage - 127.93 * voltage * voltage + 428.7 * voltage

    return tds_value


def TDSRead():
    # for i in range(0, 8):
    print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    data = ReadChannel(0)
    print("模拟信号量:", data)
    Vtrue = data * (3.3 / float(1024))   # 电源修正0.17V
    # if num_Max < Vtrue:
    #     num_Max = Vtrue
    print("电压:", Vtrue)
    Temp = temp.readTemp()
    print("温度:", Temp)
    tds = ConvertTDS(Vtrue, Temp)
    print("tds:", tds)
    # print(num_Max)


if __name__ == '__main__':
    while True:
        TDSRead()
        time.sleep(2)
