from flask import Blueprint, render_template

root_bp = Blueprint('root', __name__, url_prefix='/')

@root_bp.route('/')
def root_url():
    return render_template('root.html')