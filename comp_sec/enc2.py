from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.des import encrypt, decrypt

bp = Blueprint("enc2", __name__, url_prefix="/enc2")

# des

@bp.route("/")
def index():
    return render_template("enc2/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    submitter = request.form['submitter']
    form_data = request.form['form_data']

    parsed_form_data = parse_qs(form_data)

    if 'key' in parsed_form_data:
        key = parsed_form_data['key'][0]
        if len(key) != 8:
            return "Public Key must be 8 characters long."
    else:
        return "Public Key is a required field."

    # alice submit
    if submitter == '0':
        if 'alice_message' in parsed_form_data:
            alice_message = parsed_form_data['alice_message'][0]
            while len(alice_message) % 8 != 0:
                alice_message += " "
            encrypted_alice = ""
            decrypted_alice = ""
            for i, _ in enumerate(alice_message[::8]):
                temp_e = encrypt(alice_message[i*8:(i+1)*8],key)
                encrypted_alice += temp_e
                decrypted_alice += decrypt(temp_e,key)

            return {'alice': ["SENDING: " + alice_message, "ENCRYPT: " + encrypted_alice, "SENT---------->", ' '], 'public': ["KEY: " + key, ' ', "PUBLIC: " + encrypted_alice, ' '], 'bob': [' ', ' ', "RECIEVED: " + encrypted_alice, "DECRYPT: " + decrypted_alice]}
        else:
            return "Can not send from Alice with an empty Alice Message field."
    # bob submit
    elif submitter == '1':
        if 'bob_message' in parsed_form_data:
            bob_message = parsed_form_data['bob_message'][0]
            while len(bob_message) % 8 != 0:
                bob_message += " "
            encrypted_bob = ""
            decrypted_bob = ""
            for i, _ in enumerate(bob_message[::8]):
                temp_e = encrypt(bob_message[i*8:(i+1)*8],key)
                encrypted_bob += temp_e
                decrypted_bob += decrypt(temp_e,key)

            return {'alice': [' ', ' ', "RECIEVED: " + encrypted_bob, "DECRYPT: " + decrypted_bob], 'public': ["KEY: " + key, ' ', "PUBLIC: " + encrypted_bob, ' '], 'bob': ["SENDING: " + bob_message, "ENCRYPT: " + encrypted_bob, "<-------------SENT", ' ']}
        else:
            return "Can not send from Bob with an empty Bob Message field."
    return "ERROR"