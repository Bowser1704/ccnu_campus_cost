from routes import app
from flask import send_file
from utils.wc import generate
import os
from pathlib import Path

# 返回词云 以png方式 内联图片
@app.route("/wc/<stu_num>.png", methods=['GET'])
def wc(stu_num=None):
    dir_path = os.getcwd() + "/utils/wc/tmp/"
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    file_path = dir_path + "{stu_num}.png".format(stu_num=stu_num)
    if not Path(file_path).is_file():
        generate.generate_place(stu_num)
    return send_file(file_path, as_attachment=False)
