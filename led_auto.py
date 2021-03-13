#
import os
from datetime import time, datetime
from time import sleep
from RPi import GPIO

import gpio_init as gpio


def init():
    pass


# 到点开始，结束时间+1分钟停止
# 24h
def ledauto(setHourStart, setMinuteStart, setHourEnd, setMinuteEnd):
    ledStatus = GPIO.input(37)
    # print(ledStatus)
    # nowHour = int(time.strftime("%H", time.localtime()))
    # nowMinute = int(time.strftime("%M", time.localtime()))
    # nowS = int(time.strftime("%S",time.localtime()))

    StartTime = time(setHourStart, setMinuteStart)
    StopTime = time(setHourEnd, setMinuteEnd)
    NowTime = datetime.now().time()

    if StartTime <= NowTime <= StopTime and ledStatus == 1:
        gpio.led_start()
       # os.system("python3 Workspaces/gpio_1/AutoMakePhone.py")
        print("start")
    elif StartTime > NowTime or StopTime < NowTime and ledStatus == 0:
        gpio.led_end()
        print("End")
    else:
        print(NowTime)
    # 逻辑缺陷
    # if ledStatus == 1 and (setHourStart <= nowHour and setMinuteStart <= nowMinute) and (
    #         setMinuteEnd >= nowMinute and setHourEnd >= nowHour):
    #     gpio.led_start()
    #     print("start")
    # # elif ledStatus == 0 and (setHourEnd <= nowHour and setMinuteEnd <= nowMinute) or (ledStatus == 0 and setMinuteStart >= nowMinute and setHourStart >= nowHour):
    # #     gpio.led_end()
    # #     print("end")
    # elif ledStatus == 0 and setHourEnd <= nowHour and setMinuteEnd < nowMinute:
    #     gpio.led_end()
    #     print("111111")
    #     print("end")
    # elif ledStatus == 0 and setMinuteStart > nowMinute and setHourStart >= nowHour:
    #     gpio.led_end()
    #     print("2222222")
    #     print("end")
    # else:
    #     print(nowHour, ":", nowMinute)


if __name__ == '__main__':
    gpio.init()
    while True:
        ledauto(8, 0, 22, 30)
        sleep(1)
