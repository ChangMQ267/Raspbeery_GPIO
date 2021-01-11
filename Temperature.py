# !/usr/bin/env python
# ----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7.
#		replace the 28-XXXXXXXXX as yours.
# ----------------------------------------------------------------
import os, time, datetime, ftplib

ds18b20 = '28-21607ec4dcff'


def setup():
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i


def read():
    #	global ds18b20
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


# 将获取到的数据使用标准格式写入txt
def write_txt(eq_id):
    glass_id = "25TCFTEST1"
    folder_name = os.path.join(os.path.dirname(os.path.abspath("_file_")), "eda_file")
    start_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # end_time = (datetime.datetime.now()+datetime.timedelta(seconds=10)).strftime("%Y%m%d%H%M%S")
    file_name = "%s%s%s%s" % (eq_id, '_25TCFTEST1_SENSORS_', start_time, ".txt")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = os.path.join(folder_name, file_name)
    file = open(file_path, "w")
    file.write("HEADER_BEGIN\r\n")
    file.write("STEP_ID:STEP_SENS\r\n")
    file.write("PRODUCT_ID:PROD_SENS\r\n")
    file.write("EQP_ID:%s\r\n" % eq_id)
    file.write("GLASS_ID:%s\r\n" % glass_id)
    file.write("START_TIME:%s\r\n" % datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    file.write(
        "END_TIME:%s\r\n" % (datetime.datetime.now() + datetime.timedelta(seconds=10)).strftime("%Y/%m/%d %H:%M:%S"))
    file.write("LOT_ID:LOT_SENS\r\n")
    file.write("SHOP:CF\r\n")
    file.write("HEADER_END\r\n\r\n")
    file.write("SENSORS_DATA_BEGIN\r\n")
    file.write("PARAMETER,SN,X,Y,VALUE\r\n")
    file_path = os.path.join(folder_name, file_name)
    for x in range(10):
        # 每隔n秒读取一次数据
        time.sleep(3)
        if read() != None:
            temperature = "%0.3f" % read()
            # if read()!=None:
            # 	file.write("temperture,%s,0,0,%0.3f\n" % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), read()))
            file.write("temperture,%s,0,0,%s\r\n" % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), temperature))

    file.write("SENSORS_DATA_END\r\n\r\n")
    file.write("GLASS_SUMMARY_DATA_SENSORS_BEGIN\r\n")
    file.write("GLASS_ID,PARAMETER,AVG,STD,MAX,MIN,RANGE\r\n")
    file.write("%s,temperture,%s,%s,%s,%s,%s\r\n" % (glass_id, 22, 22, 22, 22, 22))
    file.write("GLASS_SUMMARY_DATA_SENSORS_END\r\n")
    file.close()
    return file_name, file_path


# 文件上传
# def upload(file_name, file_path):
#     host = '172.16.20.51'
#     username = 'EXP_SENSORS'
#     password = 'EXP_SENSORS'
#     file_remote = 'cimfs\\EQP\\CF\\EXP_SENSORS\\SOURCE\\%s\\%s' % (
#     datetime.datetime.now().strftime('%Y%m%d'), file_name)
#     # 实例化FTP对象
#     fp = ftplib.FTP(host)
#     fp.login(user=username, passwd=password)
#     file = open(file_path, 'rb')
#     fp.storbinary('STOR %s' % file_remote, file, 1024)
#     file.close()
#     fp.quit()


def loop():
    file_name_ls = []
    while True:
        # if read() != None:
        # temperature = "%0.3f"%read()
        file_name, file_path = write_txt("1FEXPM30")
        print(file_name, file_path)
        # upload(file_name,file_path)
        # 删除旧文件，只保留the newest 100笔文件
        file_name_ls.append(file_path)
        if len(file_name_ls) >= 20:
            if os.path.exists(file_name_ls[0]):
                os.remove(file_name_ls.pop(0))


if __name__ == '__main__':
    # try:
    setup()
    while True:
        print(read())
# except:
# 	print("program error!")