from routes import app
from flask import render_template

# 主 html
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
