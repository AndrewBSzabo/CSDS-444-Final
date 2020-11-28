from flask import Blueprint
from flask import flash
from flask import redirect
from flask import g
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.ceasar_cipher import CaesarEncrypt, CaesarDecrypt

bp = Blueprint("enc0", __name__, url_prefix="/enc0")

# Caeser

@bp.route("/", methods=("GET", "POST"))
def index():
    return render_template("enc0/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    submitter = request.form['submitter']
    form_data = request.form['form_data']

    parsed_form_data = parse_qs(form_data)
    print(parsed_form_data)

    if 'key' in parsed_form_data:
        key = parsed_form_data['key'][0]
        if not key.isdigit():
            return "Rotation Amount must be a positive integer value."
    else:
        return "Public Rotation Amount is a required field."

    # alice submit
    if submitter == '0':
        if 'alice_message' in parsed_form_data:
            alice_message = parsed_form_data['alice_message'][0]
            encrypted_alice = CaesarEncrypt(alice_message,int(key))
            return {'alice': ["SENDING: " + alice_message, "ENCRYPT: " + encrypted_alice, "SENT---------->", ' '], 'public': ["ROTATION AMOUNT: " + key, ' ', "PUBLIC: " + encrypted_alice, ' '], 'bob': [' ', ' ', "RECIEVED: " + encrypted_alice, "DECRYPT: " + CaesarDecrypt(encrypted_alice, int(key))]}
        else:
            return "Can not send from Alice with an empty Alice Message field."
    # bob submit
    elif submitter == '1':
        if 'bob_message' in parsed_form_data:
            bob_message = parsed_form_data['bob_message'][0]
            encrypted_bob = CaesarEncrypt(bob_message,int(key))
            return {'alice': [' ', ' ', "RECIEVED: " + encrypted_bob, "DECRYPT: " + CaesarDecrypt(encrypted_bob, int(key))], 'public': ["ROTATION AMOUNT: " + key, ' ', "PUBLIC: " + encrypted_bob, ' '], 'bob': ["SENDING: " + bob_message, "ENCRYPT: " + encrypted_bob, "<-------------SENT", ' ']}
        else:
            return "Can not send from Bob with an empty Bob Message field."
    return "ERROR"