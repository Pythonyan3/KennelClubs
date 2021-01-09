from app.main import main_blueprint
from flask import render_template, send_file

from app.main.utils import clubs_addresses, possible_rewards


@main_blueprint.route('/', methods=['GET'])
def index():
    clubs = clubs_addresses()
    rewards = possible_rewards()
    return render_template('main/index.html', clubs=clubs, rewards=rewards)


@main_blueprint.route('/report', methods=['GET'])
def report():
    return send_file('static/docs/report.xlsx', cache_timeout=-1)
