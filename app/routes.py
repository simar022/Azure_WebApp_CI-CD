from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', title="Home")

@main_bp.route('/status')
def status():
    return {"status": "online", "environment": "Azure Web App", "containerized": True}
