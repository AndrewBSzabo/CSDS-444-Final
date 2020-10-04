from flask import Blueprint
from flask import flash
from flask import redirect
from flask import g
from flask import render_template
from flask import request
from flask import url_for

from comp_sec.algs.vigenere_cipher import encrypt, decrypt

bp = Blueprint("enc1", __name__, url_prefix="/enc1")


@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        if 'enc' in request.form:
            to_enc = request.form["to_enc"]
            key = request.form["key"]

            return encrypt(to_enc, key)
        if 'dec' in request.form:
            to_dec = request.form["to_dec"]
            key = request.form["key"]

            return decrypt(to_dec, key)
    return render_template("enc1/index.html")