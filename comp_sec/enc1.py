from flask import Blueprint
from flask import flash
from flask import redirect
from flask import g
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

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

    parsed_form_data = parse_qs(form_data)

    alice_message = parsed_form_data['alice_message'][0]
    bob_message = parsed_form_data['bob_message'][0]
    key = parsed_form_data['key'][0]

    encrypted_bob = encrypt(bob_message,key)
    encrypted_alice = encrypt(alice_message,key)

    # alice submit
    if submitter == '0':
        return {'alice': ["SENDING: " + alice_message, "ENCRYPT: " + encrypted_alice,"SENT---------->", ' '], 'public': ["KEY: " + key,' ',"PUBLIC: " + encrypted_alice, ' '], 'bob': [' ',' ',"RECIEVED: " + encrypted_alice, "DECRYPT: " + decrypt(encrypted_alice, key)]}
    # bob submit
    elif submitter == '1':
        return {'alice': [' ',' ',"RECIEVED: " + encrypted_bob, "DECRYPT: " + decrypt(encrypted_bob, key)], 'public': ["KEY: " + key,' ',"PUBLIC: " + encrypted_bob, ' '], 'bob': ["SENDING: " + bob_message, "ENCRYPT: " + encrypted_bob,"<-------------SENT", ' ']}
    return "ERROR"

