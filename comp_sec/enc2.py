from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

bp = Blueprint("enc2", __name__, url_prefix="/enc2")

# des

@bp.route("/")
def index():
    return render_template("enc2/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    pass