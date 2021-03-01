# /usr/bin/python3

from RPi import GPIO

import gpio_init as gpio
import Temperature as temp
import time


def tempauto(MinTemp, MaxTemp):
    # GPIO.setmode(GPIO.BOARD)
    while True:
        nowTemp = temp.readTemp()
        print("当前温度为:%.3f" % nowTemp, "设定最低温度为:%.3f" % MinTemp, "设定最高温度为:%.3f" % MaxTemp)
        if nowTemp < MinTemp:
            gpio.add_temp()
            print("开启加热")
        elif nowTemp > MaxTemp:
            gpio.stop_add_temp()
            print("停止加热")
        else:
            pass
        time.sleep(5)


if __name__ == '__main__':
    gpio.init()
    gpio.add_oxy()
    gpio.water_start()
    tempauto(22.5, 23)
