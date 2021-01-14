# /usr/bin/python3

from RPi import GPIO

import gpio_init as gpio
import Temperature as temp
import time

def tempauto(setTemp):
    # GPIO.setmode(GPIO.BOARD)
    while True:
        nowTemp = temp.readTemp()
        print("当前温度为:%f" % nowTemp, "设定温度为:%f" % setTemp)
        if nowTemp < setTemp:
            gpio.add_temp()
            print("开启加热")
        else:
            gpio.stop_add_temp()
            print("停止加热")
        time.sleep(5)


if __name__ == '__main__':
    gpio.init()
    gpio.add_oxy()
    gpio.water_start()
    tempauto(22)
