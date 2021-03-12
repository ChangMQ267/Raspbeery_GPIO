# /usr/bin/python3
import time

import gpio_init
import TempAuto
import Temperature
import TDS
import video
from led_auto import ledauto

MinTemp = 22.9
MaxTemp = 23
SetHourStart = 8
SetMinuteStart = 0
SetHourEnd = 22
SetMinuteEnd= 30

if __name__ == '__main__':
    gpio_init.init()
    #gpio_init.add_oxy()
   # video.video_start()
    while True:
        ledauto(SetHourStart,SetMinuteStart,SetHourEnd,SetMinuteEnd)
        temp = TempAuto.tempauto(MinTemp, MaxTemp)
        TDS.TDSRead()
        time.sleep(5)
