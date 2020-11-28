from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.md5 import encrypt

bp = Blueprint("enc4", __name__, url_prefix="/enc4")

# MD5

@bp.route("/",methods=("GET", "POST"))
def index():
    return render_template("enc4/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    submitter = request.form['submitter']
    form_data = request.form['form_data']

    parsed_form_data = parse_qs(form_data)

    # alice submit
    if submitter == '0':
        if 'alice_message' in parsed_form_data:
            alice_message = parsed_form_data['alice_message'][0]
            encrypted_alice = encrypt(alice_message)
            return {'alice': ["SENDING: " + alice_message, "HASH: " + encrypted_alice, "SENT---------->", ' '], 'public': [' ', ' ', "PUBLIC: " + encrypted_alice, ' '], 'bob': ['EXPECTED: ' + encrypted_alice, ' ', "RECIEVED: " + encrypted_alice, "RECIEVED VALID HASH"]}
        else:
            return "Can not send from Alice with an empty Alice Message field."
    # bob submit
    elif submitter == '1':
        if 'bob_message' in parsed_form_data:
            bob_message = parsed_form_data['bob_message'][0]
            encrypted_bob = encrypt(bob_message)
            return {'alice': ['EXPECTED: ' + encrypted_bob, ' ', "RECIEVED: " + encrypted_bob, "RECIEVED VALID HASH"], 'public': [' ', ' ', "PUBLIC: " + encrypted_bob, ' '], 'bob': ["SENDING: " + bob_message, "HASH: " + encrypted_bob, "<-------------SENT", ' ']}
        else:
            return "Can not send from Bob with an empty Bob Message field."
    return "ERROR"
