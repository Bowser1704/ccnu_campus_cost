from flask import Flask, render_template, jsonify

import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route("/l1")
def get_l1_data():
    data=utils.get_l1_data()
    cost,time=[],[]
    for a,b in data[0::10]:

        cost.append(a)
        time.append(b[6:10])

    return jsonify({"day":time,"cost":cost})

@app.route("/l2")
def get_l2_data():
    data=utils.get_l2_data()
    cost,time=[],[]
    for a,b in data[0::10]:

        cost.append(a)
        time.append(b[6:10])

    return jsonify({"day":time,"cost":cost})

@app.route("/r1")
def get_r1_data():
    data=utils.get_r1_data()
    cost,time=[],[]
    for a,b in data[0::10]:

        cost.append(a)
        time.append(b[6:10])

    return jsonify({"day":time,"cost":cost})

@app.route("/r2")
def get_r2_data():
    data=utils.get_r2_data()
    cost,time=[],[]
    for a,b in data[0::10]:

        cost.append(a)
        time.append(b[6:10])

    return jsonify({"day":time,"cost":cost})


if __name__ == '__main__':
    app.run()
