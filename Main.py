# /usr/bin/python3
import time

import gpio_init
import TempAuto
import TDS
import video
from dbUtils import water_status_db
from led_auto import ledauto

MinTemp = 22.9
MaxTemp = 23
SetHourStart = 8
SetMinuteStart = 0
SetHourEnd = 22
SetMinuteEnd = 30

if __name__ == '__main__':
    gpio_init.init()
    #gpio_init.add_oxy()
    video.video_start()

    while True:
        temp = 0.0
        TDSNum = 0.0
        ledauto(SetHourStart, SetMinuteStart, SetHourEnd, SetMinuteEnd)
        temp = TempAuto.tempauto(MinTemp, MaxTemp)
        TDSNum = TDS.TDSRead()
        if temp == 0.0 or TDSNum == 0.0 :
            water_status_db(temp,TDSNum)
        time.sleep(5)
