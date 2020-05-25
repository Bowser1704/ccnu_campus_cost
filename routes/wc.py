from routes import app
from flask import send_file
from utils.wc import generate
import os
from pathlib import Path


@app.route("/wc/<stunum>.png", methods=['GET'])
def wc(stunum=None):
    file_path = os.getcwd() + "/utils/wc/tmp/{stunum}.png".format(stunum=stunum)
    if not Path(file_path).is_file():
        generate.generate_place(stunum)
    return send_file(file_path, as_attachment=True)
