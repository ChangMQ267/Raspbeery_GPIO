# /usr/bin/python3
# -*- coding: UTF-8 -*-
from RPi import GPIO

import gpio_init as gpio
import Temperature as temp
import time


def tempauto(MinTemp, MaxTemp):
    # GPIO.setmode(GPIO.BOARD)
    # while True:
    temp_status = GPIO.input(36)
    # print(temp_status)
    nowTemp = temp.readTemp()
    # print("当前温度为:%.3f" % nowTemp, "设定最低温度为:%.3f" % MinTemp, "设定最高温度为:%.3f" % MaxTemp)
    if nowTemp < MinTemp and temp_status == 0:
        gpio.add_temp()
        temp_status = 1
        print("开启加热")
    elif nowTemp > MaxTemp and temp_status == 1:
        gpio.stop_add_temp()
        temp_status = 0
        print("停止加热")
    else:
        pass
    # time.sleep(5)
    return nowTemp


if __name__ == '__main__':
    gpio.init()
    gpio.add_oxy()
    gpio.water_start2()
    # gpio.water_end2()
    gpio.water_start1()
    while True:
        tempauto(22.9, 23)
        time.sleep(5)
