from app import app
from flask import render_template, send_file


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/report', methods=['GET'])
def report():
    return send_file('static/docs/report.xlsx', cache_timeout=-1)
