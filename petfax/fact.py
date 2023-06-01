from flask import ( Blueprint, render_template )
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")

# index route
@bp.route('/new')
def index():
  return render_template('facts.html')