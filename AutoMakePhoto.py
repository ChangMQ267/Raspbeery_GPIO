import os
import time


def makephoto(home,i=1):

    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    local = home + "USUA" + "_" + str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
    os.system("raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
    print("No:%d " % i + "raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
    i = i + 1
    time.sleep(10)


if __name__ == '__main__':
    home = "./Data/USUA/" + str(time.strftime("%Y-%m-%d", time.localtime())) + "/"
    os.system("mkdir -p %s" % home)
    makephoto(home)
