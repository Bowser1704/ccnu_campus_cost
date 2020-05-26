import pymysql
from flask import jsonify


def get_conn():
<<<<<<< HEAD
    conn = pymysql.connect(host="127.0.0.1",
=======
<<<<<<< HEAD
    conn = pymysql.connect(host="localhost",
=======
    conn = pymysql.connect(host="127.0.0.1",
>>>>>>> 7424e1c... feat: add db func
>>>>>>> cda0e9c65e6e7bfcc079e49e66e5575e575497f5
                           user="",
                           password="",
                           db="",
                           charset="utf8")

    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_l1_data():
    sql="select cost,time from stu3 where stunum='2016210001'"
    res=query(sql)
    return res
def get_l2_data():
    sql="select cost,time from stu3 where stunum='2016210002'"
    res=query(sql)
    return res
def get_r1_data():
    sql="select cost,time from stu3 where stunum='2016210003'"
    res=query(sql)
    return res
def get_r2_data():
    sql="select cost,time from stu3 where stunum='2016210004'"
    res=query(sql)
    return res



if __name__=="__main__":
<<<<<<< HEAD
    print(get_r1_data())
=======
    print(get_r1_data())
>>>>>>> cda0e9c65e6e7bfcc079e49e66e5575e575497f5
