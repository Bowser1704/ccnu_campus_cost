from routes import db
import models


#
def resultproxy2dict(resultproxy):
    return [{column: value for column, value in rowproxy.items()} for rowproxy in resultproxy]


# 不需要返回对象
# def dict2obj(dict_list):
#     if len(dict_list) > 1:
#         obj_list = []
#         for i in dict_list:
#             obj = models.Cost()
#             for r in dict_list.keys():
#                 obj.__setattr__(r, dict_list[r])
#             obj_list.append(obj)
#         return obj_list
#     else:
#         obj = models.Cost()
#         dic = dict_list[0]
#         for r in dic.keys():
#             obj.__setattr__(r, dic[r])
#         return obj


def result2dict(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        dict_list = resultproxy2dict(result)
        return dict_list[0] if len(dict_list) == 1 else dict_list

    return wrapper


# 返回 19 年第一次消费记录

@result2dict
def get_first_data(stu_num):
    first_sql = "select * from  stu3 where stunum = '{stu_num}' and time = (select min(time) from stu3 where stunum = " \
                "'{stu_num}');".format(
        stu_num=stu_num)
    result = db.engine.execute(first_sql)
    return result


# 返回 19 年最后一次消费记录

@result2dict
def get_last_data(stu_num):
    last_sql = "select * from  stu3 where stunum = '{stu_num}' and time = (select max(time) from stu3 where stunum = '{stu_num}');".format(
        stu_num=stu_num)
    result = db.engine.execute(last_sql)
    return result


# 返回 19 年消费总金额

@result2dict
def get_cost_sum(stu_num):
    sum_sql = "select sum(cost) from stu3 where stunum = '{stu_num}'".format(
        stu_num=stu_num)
    result = db.engine.execute(sum_sql)
    return result


# 返回 最常去的 餐厅 和 窗口。

@result2dict
def get_most_restaurant(stu_num):
    sql = "SELECT restaurant,place FROM stu3 WHERE stunum = '{stu_num}' GROUP BY restaurant,place ORDER BY COUNT(*) DESC LIMIT 1".format(
        stu_num=stu_num)
    result = db.engine.execute(sql)
    return result


# 返回 消费排行榜

@result2dict
def get_cost_rank():
    sql = "SELECT stunum,sum(`cost`)AS costsum FROM stu3 GROUP BY stunum ORDER BY costsum DESC LIMIT 10"

    result = db.engine.execute(sql)
    return result


# 返回窗口排行榜
@result2dict
def get_restaurant_place_rank():
    sql = "select restaurant, place, count(*) from stu3 group by restaurant,place order by count(*) desc limit 10"
    result = db.engine.execute(sql)
    return result


def get_restaurant_list(stu_num):
    sql = "select restaurant from stu3 where stunum = '{stu_num}'".format(stu_num=stu_num)
    result = db.engine.execute(sql)
    return [i[0].replace("餐厅", "") for i in result]


def get_place_list(stu_num):
    sql = "select place from stu3 where stunum = '{stu_num}'".format(stu_num=stu_num)
    result = db.engine.execute(sql)
    return [i[0] for i in result]


# 通过学号 返回 食堂次数排名。

@result2dict
def get_restaurant_rank(stu_num):
    sql = "select restaurant,count(*) from stu3 where stunum = '{stu_num}' group by restaurant order by count(*) desc".format(
        stu_num=stu_num)
    result = db.engine.execute(sql)
    return result
