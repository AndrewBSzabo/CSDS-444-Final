from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

bp = Blueprint("enc3", __name__, url_prefix="/enc3")

# rsa

@bp.route("/")
def index():
    return "enc3 page"