from routes import app
from models import model
from flask import jsonify


# 返回2019年第一次消费记录
@app.route('/api/record/first/<stu_num>', methods=['GET'])
def first(stu_num=None):
    return jsonify(model.get_first_data(stu_num))


# 返回2020年最后一次消费记录
@app.route('/api/record/last/<stu_num>', methods=['GET'])
def last(stu_num=None):
    return jsonify(model.get_last_data(stu_num))


# 返回食堂消费次数排名
@app.route('/api/rank/restaurant/<stu_num>', methods=['GET'])
def restaurant_rank(stu_num=None):
    return jsonify(model.get_restaurant_rank(stu_num))


# 返回某人每周消费金额
@app.route('/api/cost/list/week/<stu_num>', methods=['GET'])
def cost_list(stu_num=None):
    return jsonify(model.get_sum_every_week(stu_num))


# 返回某人 19年消费金额
@app.route('/api/cost/sum/<stu_num>', methods=['GET'])
def cost(stu_num=None):
    return jsonify(model.get_cost_sum(stu_num))


# 返回某人最爱的窗口
@app.route('/api/place/<stu_num>', methods=['GET'])
def place(stu_num=None):
    return jsonify(model.get_most_restaurant(stu_num))


# 返回所有人消费金额的排行
@app.route('/api/rank/cost', methods=['GET'])
def cost_rank():
    return jsonify(model.get_cost_rank())


# 返回所有窗口的消费排行
@app.route('/api/rank/place', methods=['GET'])
def place_rank():
    return jsonify(model.get_restaurant_place_rank())
