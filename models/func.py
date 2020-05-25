from models import db

# 返回 19 年第一次消费记录


def get_first_data(stunum):
    first_sql = "select * from  stu3 where stunum = '{stunum}' and time = (select min(time) from stu3 where stunum = '{stunum}');".format(
        stunum=stunum)
    result = db.engine.execute(first_sql)
    return result.first()

# 返回 19 年最后一次消费记录


def get_last_data(stunum):
    last_sql = "select * from  stu3 where stunum = '{stunum}' and time = (select max(time) from stu3 where stunum = '{stunum}');".format(
        stunum=stunum)
    result = db.engine.execute(last_sql)
    return result.first()

# 返回 19 年消费总金额


def get_cost_sum(stunum):
    sum_sql = "select sum(cost) from stu3 where stunum = '{stunum}'".format(
        stunum=stunum)
    result = db.engine.execute(sum_sql)
    return result.first()

# 返回 最常去的 餐厅 和 窗口。


def get_most_restaurant(stunum):
    sql = "SELECT restaurant,place FROM stu3 WHERE stunum = '{stunum}' GROUP BY restaurant,place ORDER BY COUNT(*) DESC LIMIT 1".format(
        stunum=stunum)
    result = db.engine.execute(sql)
    return result.first()

# 返回 消费排行榜


def get_cost_rank(stunum):
    sql = "SELECT stunum,sum(`cost`)AS costsum FROM stu3 GROUP BY stunum ORDER BY costsum DESC LIMIT 30"
    result = db.engine.execute(sql)
    return [i for i in result]

# 返回窗口排行榜

def get_restaurant_rank(stunum):
    sql = "select restaurant, place, count(*) from stu3 group by restaurant,place order by count(*) desc limit 10"
    result = db.engine.execute(sql)
    return [i for i in result]