# /usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import time

width = 1920
height = 1080


def photo_eat():
    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    home = "./Data/EAT/" + str(time.strftime("%Y-%m-%d", time.localtime())) + "/"
    os.system("mkdir -p %s" % home)
    for i in range(3 * 60):
        local = home + "eat_" + str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        os.system("raspistill -o %s.jpg -w %d -h %d -t 1000" % (local, width, height))
        print("No:%d " % i + "raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
        # time.sleep(0.5)


def photo(status, num):
    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    home = "./Data/" + str(time.strftime("%Y-%m-%d", time.localtime())) + "/"
    os.system("mkdir -p %s" % home)
    for i in range(num):
        local = home + status + "_" + str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        os.system("raspistill -o %s.jpg -w %d -h %d -t 1000" % (local, width, height))
        print("No:%d " % i + "raspistill -o %s.jpg -w 1280 -h 720 -t 10000" % local)
        time.sleep(1)


if __name__ == '__main__':
    print("取样类型：1:normal 2:eat")
    key = input()
    if key == "1":
        status = "normal"
    elif key == "2":
        status = "eat"
    else:
        status = "NULL"
    print("取样次数：")
    num = int(input())
    photo(status, num)
