from routes import app
from models import model
from flask import jsonify


@app.route('/api/record/first/<stu_num>', methods=['GET'])
def first(stu_num=None):
    return jsonify(model.get_first_data(stu_num))


@app.route('/api/record/last/<stu_num>', methods=['GET'])
def last(stu_num=None):
    return jsonify(model.get_last_data(stu_num))


@app.route('/api/cost/sum/<stu_num>', methods=['GET'])
def cost(stu_num=None):
    return jsonify(model.get_cost_sum(stu_num))


@app.route('/api/place/<stu_num>', methods=['GET'])
def place(stu_num=None):
    return jsonify(model.get_most_restaurant(stu_num))


@app.route('/api/rank/cost', methods=['GET'])
def cost_rank():
    return jsonify(model.get_cost_rank())


@app.route('/api/rank/place', methods=['GET'])
def place_rank():
    return jsonify(model.get_restaurant_place_rank())


@app.route('/api/rank/restaurant/<stu_num>', methods=['GET'])
def restaurant_rank(stu_num=None):
    return jsonify(model.get_restaurant_rank(stu_num))
