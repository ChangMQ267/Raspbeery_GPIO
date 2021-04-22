# /usr/bin/python3
# -*- coding: UTF-8 -*-
import time

import Temperature
import gpio_init
import TempAuto
import TDS
import video
from AutoOXY import oxyauto
from dbUtils import water_status_db
from led_auto import ledauto

MinTemp = 22.9
MaxTemp = 23
SetHourStart = 8
SetMinuteStart = 0
SetHourEnd = 21
SetMinuteEnd = 30
OxyStartHour = 7
OxyStartMinute = 30
OxyStopHour = 10
OxyStopMinute = 30
if __name__ == '__main__':
    gpio_init.init()
    gpio_init.add_oxy()
    video.video_start()
    gpio_init.stop_add_temp()
    # gpio_init.eat()
    # gpio_init.water_end2()
    status = 1
    while True:
        temp = 0.0
        TDSNum = 0.0
        ledauto(SetHourStart, SetMinuteStart, SetHourEnd, SetMinuteEnd)
        oxyauto(OxyStartHour,OxyStartMinute,OxyStopHour,OxyStopMinute)
        temp = TempAuto.tempauto(MinTemp, MaxTemp)
        #temp = Temperature.readTemp()
        TDSNum = TDS.TDSRead()
        print("temp:", temp, "   ", "tds:", TDSNum)
        # if temp == 0.0 or TDSNum == 0.0 or status == 1:
        #     status = 0
        #     continue
        # else:
        #     water_status_db(temp, TDSNum)
        time.sleep(3)
