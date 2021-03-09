# /usr/bin/python3
import time

import gpio_init
import TempAuto
import Temperature
import TDS
import video

MinTemp = 22.9
MaxTemp = 23


if __name__ == '__main__':
    gpio_init.init()
    gpio_init.led_start()
    #gpio_init.add_oxy()
    while True:
        temp = TempAuto.tempauto(MinTemp, MaxTemp)
        TDS.TDSRead()
        time.sleep(5)
