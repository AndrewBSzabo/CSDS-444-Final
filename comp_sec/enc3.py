from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.rsa import encrypt, decrypt, getConsts

bp = Blueprint("enc3", __name__, url_prefix="/enc3")

# rsa

@bp.route("/",methods=("GET","POST"))
def index():
    return render_template("enc3/index.html")

@bp.route("/encrypter", methods=("GET", "POST"))
def encrypter():
    submitter = request.form["submitter"]
    form_data = request.form["form_data"]

    parsed_form_data = parse_qs(form_data)

    p, q, n, nt, e, d = getConsts()
    p, q, n, nt, e, d = str(p), str(q), str(n), str(nt), str(e), str(d)

    # alice submit
    if submitter == "0":
        if "alice_message" in parsed_form_data:
            alice_message = parsed_form_data["alice_message"][0]
            encrypted_alice = encrypt(alice_message)
            return {"alice": [" ", " ", " ", " ", " ", " ", " ", "SENDING: " + alice_message, "ENCRYPT: " + encrypted_alice, "SENT---------->", " "], "public": ["p = " + p, "q = " + q, "e = " + e, " ", "CALCULATIONS:", "n = p * n = " + n, "totient_n = " + nt, " ", " ", "PUBLIC: " + encrypted_alice, " "], "bob": [" ", " ", " ", " ", "CALCULATIONS:", "b = " + d + ", (from: 1 = e * d mod totient_n)", " ", " ", " ", "RECIEVED: " + encrypted_alice, "DECRYPT: " + decrypt(encrypted_alice)]}
        else:
            return "Can not send from Alice with an empty Alice Message field."
    # bob submit
    elif submitter == "1":
        if "bob_message" in parsed_form_data:
            bob_message = parsed_form_data["bob_message"][0]
            encrypted_bob = encrypt(bob_message)
            return {"alice": [" ", " ", " ", " ", "CALCULATIONS:", "b = " + d + ", (from: 1 = e * d mod totient_n)", " ", " ", " ", "RECIEVED: " + encrypted_bob, "DECRYPT: " + decrypt(encrypted_bob)], "public": ["p = " + p, "q = " + q, "e = " + e, " ", "CALCULATIONS:", "n = p * n = " + n, "totient_n = " + nt, " ", " ", "PUBLIC: " + encrypted_bob, " "], "bob": [" ", " ", " ", " ", " ", " ", " ", "SENDING: " + bob_message, "ENCRYPT: " + encrypted_bob, "<-------------SENT", " "]}
        else:
            return "Can not send from Bob with an empty Bob Message field."
    return "ERROR"
