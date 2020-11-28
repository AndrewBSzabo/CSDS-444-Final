from flask import Blueprint
from flask import flash
from flask import redirect
from flask import g
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.vigenere_cipher import encrypt, decrypt

bp = Blueprint("enc0", __name__, url_prefix="/enc0")

# Caeser

@bp.route("/", methods=("GET", "POST"))
def index():
    return render_template("enc0/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    pass