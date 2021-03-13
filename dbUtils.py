import pymysql as mysql
from datetime import datetime, time


def water_status_db(temperature, tds):
    db = mysql.connect(host="172.28.212.201", user="develop", password="develop", database="fishmanager",
                       charset="utf8mb4")
    # conn = MySQLd.connect("localhost", "root", "123456", "fish_know", charset="utf8mb4")
    cursor = db.cursor()
    # sql = "select * from water_status"
    print(datetime.now())
    sql = "INSERT INTO water_status(datetime,temp, tds) VALUES ('%s','%f','%f')" % (
    datetime.now(), temperature, tds)
    cursor.execute(sql)
    db.commit()
    # try:
    # # 执行sql语句
    #     cursor.execute(sql)
    # # 执行sql语句
    #     db.commit()
    # except:
    # # 发生错误时回滚
    #     db.rollback()
    #     print("bug")
    # # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    water_status_db(23, 400)
