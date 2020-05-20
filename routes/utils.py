import pymysql
from flask import jsonify


def get_conn():
    conn = pymysql.connect(host="47.100.3.74",
                           user="pystudyuser",
                           password="pystudyuser",
                           db="stu_data",
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
    print(get_r1_data())