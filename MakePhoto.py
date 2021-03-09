# /usr/bin/python3

import os
import time


# #raspistill 是树莓派基于摄像头拍照命令
#
# 比如我要截取一张宽1024px，高768px，旋转180度的图片，抓取的总时长为20秒，并且每5秒抓取一张，保存的文件名为image1.jpg,image2.jpg以此类推。
#
# 命令如下:
#
# sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v
# raspistill 常用参数如下
#
# -v：调试信息查看。
# -w：图像宽度
# -h：图像高度
# -rot：图像旋转角度，只支持 0、90、180、270 度
# -o：图像输出地址，例如image.jpg，如果文件名为“-”，将输出发送至标准输出设备
# -t:获取图像前等待时间，默认为5000，即5秒
# -tl：多久执行一次图像抓取。
#
# 默认-t参数等于5000，即会拍照前等待5秒钟。
def photo_eat():
    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    home = "./Data/EAT/" + str(time.strftime("%Y-%m-%d", time.localtime())) + "/"
    os.system("mkdir -p %s" % home)
    for i in range(3*60):
        local = home + "eat_" + str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        os.system("raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
        print("No:%d " % i + "raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
        #time.sleep(0.5)


def photo(status, num):
    # os.system("sudo raspistill -o image%d.jpg -rot 180 -w 1024 -h 768 -t 20000 -tl 5000 -v"%num);
    home = "./Data/" + str(time.strftime("%Y-%m-%d", time.localtime())) + "/"
    os.system("mkdir -p %s" % home)
    for i in range(num):
        local = home + status + "_" + str(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        os.system("raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
        print("No:%d " % i + "raspistill -o %s.jpg -w 1280 -h 720 -t 1000" % local)
        #time.sleep(1)


if __name__ == '__main__':
    print("取样状态：1:normal 2:eat")
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
