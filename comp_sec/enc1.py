from flask import Blueprint
from flask import flash
from flask import redirect
from flask import g
from flask import render_template
from flask import request
from flask import url_for
import re

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


@bp.route("/new_lander", methods=("GET", "POST"))
def new_lander():
    return render_template("enc1/new_lander.html")


@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    submitter = request.form['submitter']
    form_data = request.form['form_data']

    alice_message = re.findall(r'alice_message=(.*?)&|$', form_data)[0]
    bob_message = re.findall(r'bob_message=(.*?)&|$', form_data)[0]
    key = re.findall(r'key=(.*?)&|$', form_data)[0]

    # alice submit
    if submitter == '0':
        return {'alice': alice_message, 'public': key, 'bob': "ENCRYPTED:" + alice_message}
    # bob submit
    elif submitter == '1':
        return {'alice': "ENCRYPTED:" + bob_message, 'public': '', 'bob': bob_message}
    return "ERROR"

