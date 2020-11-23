from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from comp_sec.algs.rsa import encrypt, decrypt

bp = Blueprint("enc3", __name__, url_prefix="/enc3")

# rsa

@bp.route("/",methods=("GET","POST"))
def index():
    if request.method == "POST":
        if 'enc' in request.form:
            to_enc = request.form["to_enc"]

            return encrypt(to_enc)
        if 'dec' in request.form:
            to_dec = request.form["to_dec"]

            return decrypt(to_dec)
    return render_template("enc3/index.html")
