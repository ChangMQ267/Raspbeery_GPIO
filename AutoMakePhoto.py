# /usr/bin/python3
# -*- coding: UTF-8 -*-
import os

from datetime import datetime, time
from time import strftime, localtime, sleep


def makephoto(home):
    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    local = home + "USUA" + "_" + str(strftime("%Y-%m-%d_%H:%M:%S", localtime()))
    os.system("raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
    print("raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
    sleep(10)


if __name__ == '__main__':
    home = "./Data/USUA/" + str(strftime("%Y-%m-%d", localtime())) + "/"
    os.system("mkdir -p %s" % home)
    # print (time(8,30))
    while time(8, 30) <= datetime.now().time() <= time(21, 30):
        makephoto(home)
