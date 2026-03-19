from flask import Blueprint, render_template
from .models import add_visit_log, get_logs

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    add_visit_log()
    recent_logs = get_logs()
    return render_template('index.html', title="Home", logs=recent_logs)

@main_bp.route('/status')
def status():
    return {"status": "online", "environment": "Azure Web App", "containerized": True}
