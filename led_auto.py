#
import time

from RPi import GPIO

import gpio_init as gpio


def init():
    pass


def ledauto(setHourStart, setMinuteStart, setHourEnd, setMinuteEnd):
    ledStatus = GPIO.input(37)
    print(ledStatus)
    nowHour = int(time.strftime("%H", time.localtime()))
    nowMinute = int(time.strftime("%M", time.localtime()))
    nowS = int(time.strftime("%S",time.localtime()))
    if ledStatus == 1 and (setHourStart <= nowHour and setMinuteStart <= nowMinute) and (
            setMinuteEnd >= nowMinute and setHourEnd >= nowHour):
        gpio.led_start()
        print("start")
    # elif ledStatus == 0 and (setHourEnd <= nowHour and setMinuteEnd <= nowMinute) or (ledStatus == 0 and setMinuteStart >= nowMinute and setHourStart >= nowHour):
    #     gpio.led_end()
    #     print("end")
    elif ledStatus == 0 and setHourEnd <= nowHour and setMinuteEnd <= nowMinute:
        gpio.led_end()
        print("end")
    elif ledStatus == 0 and setMinuteStart >= nowMinute and setHourStart >= nowHour:
        gpio.led_end()
        print("end")
    else:
        print(nowHour, ":", nowMinute)


if __name__ == '__main__':
    gpio.init()
    while True:
        ledauto(20, 41, 20, 42)
        time.sleep(1)
