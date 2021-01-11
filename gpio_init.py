# 初始化GPIO模块
# import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time
#import led_auto
#from apscheduler.schedulers.blocking import BlockingScheduler

# 32: 换水装置1
# 35: 投食机器
# 36: 加热棒
# 37: 灯管
# 38: 增氧
# 40: 换水
USE_GPIO_OUT_NUM = [32, 35, 36, 37, 38, 40]

# 22:
# 23:
USE_GPIO_IN_NUM = [22, 23]


def init():
    print("系统初始化开始。。。")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    print("MODE SET BOARD")
    for i in USE_GPIO_OUT_NUM:
        GPIO.setup(i, GPIO.OUT)
        print(i, "模式设置为:OUT")
        GPIO.output(i, True)
        print(i, "值设置为:", True)
    print("初始化启动完成。")

def led_start():
    GPIO.output(37, False)


# GPIO.

def led_end():
    GPIO.output(37, True)

def gpio_32():
    GPIO.output(32,True)

def firsr_start():
    led_start()
    water_start()
    print("已启动照明、换水装置！")

def water_start():
    GPIO.output(32, False)


def water_end():
    GPIO.output(32, True)


def eat():
    GPIO.output(35, False)
    time.sleep(1)
    GPIO.output(35, True)


def led_auto():
    time_now = time.time()
    print(time_now)

def add_oxy():
    GPIO.output(38,False)

def stop_add_oxy():
    GPIO.output(38, True)

def GPIO_init():
    GPIO.cleanup()

if __name__ == '__main__':

    init()
    # print("初始化完成\n")
    #led_auto()
    #water_end()
  # led_start()
    add_oxy()
    water_start()
    #GPIO.output(32,False)
    #GPIO.cleanup()
    while True :
        key = input()
        if key == "开灯":
            led_start()
        elif key == "关灯":
            led_end()
        elif key == "投食":
            eat()
        elif key =="换水":
            water_start()
            # time.sleep(10)
            # water_end()
        elif key =="停止换水":
            water_end()
        else:
            #GPIO.cleanup()
            print("系统已关闭 "
                  ""
                  ""
                  "")
            break
