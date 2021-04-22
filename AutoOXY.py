# /usr/bin/python3
# -*- coding: UTF-8 -*-
import os
from datetime import time, datetime
from time import sleep
from RPi import GPIO

import gpio_init as gpio


def oxyauto(setHourStart, setMinuteStart, setHourEnd, setMinuteEnd):
    oxyStatus = GPIO.input(38)
    # print(ledStatus)
    # nowHour = int(time.strftime("%H", time.localtime()))
    # nowMinute = int(time.strftime("%M", time.localtime()))
    # nowS = int(time.strftime("%S",time.localtime()))

    StartTime = time(setHourStart, setMinuteStart)
    StopTime = time(setHourEnd, setMinuteEnd)
    NowTime = datetime.now().time()

    if StartTime <= NowTime <= StopTime and oxyStatus == 1:
        gpio.add_oxy()
        # os.system("python3 Workspaces/gpio_1/AutoMakePhone.py")
        print("OXY start")
    elif StartTime > NowTime or StopTime < NowTime and oxyStatus == 0:
        gpio.stop_add_oxy()
        print("OXY End")
    else:
        pass
