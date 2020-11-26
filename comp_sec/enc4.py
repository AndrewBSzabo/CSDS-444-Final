from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from comp_sec.algs.md5 import encrypt

bp = Blueprint("enc4", __name__, url_prefix="/enc4")

# MD5

@bp.route("/",methods=("GET", "POST"))
def index():
    if request.method == "POST":
        if 'enc' in request.form:
            to_enc = request.form["to_enc"]
            return encrypt(to_enc)

    return render_template("enc4/index.html")
