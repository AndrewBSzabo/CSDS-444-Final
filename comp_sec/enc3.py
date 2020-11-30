from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from urllib.parse import parse_qs

from comp_sec.algs.rsa import encrypt, decrypt, getConstsAlice, getConstsBob

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

    a_p, a_q, a_n, a_nt, a_e, a_d = getConstsAlice()
    a_p, a_q, a_n, a_nt, a_e, a_d = str(a_p), str(a_q), str(a_n), str(a_nt), str(a_e), str(a_d)

    b_p, b_q, b_n, b_nt, b_e, b_d = getConstsBob()
    b_p, b_q, b_n, b_nt, b_e, b_d = str(b_p), str(b_q), str(b_n), str(b_nt), str(b_e), str(b_d)

    # alice submit
    if submitter == "0":
        if "alice_message" in parsed_form_data:
            alice_message = parsed_form_data["alice_message"][0]
            encrypted_alice = encrypt(alice_message, int(b_e), int(b_n))
            return {"alice": ["ALICE VARIABLES:", "a_p = " + a_p, "a_q = " + a_q, "a_n = a_p * a_q = " + a_n, "totient(a_n) = " + a_nt, "a_e = " + a_e, "a_d = " + a_d + " (from: 1 = a_e * a_d mod totient(a_n))", "SENDING: " + alice_message, "ENCRYPT (using c = m ^ b_e mod b_n): " + encrypted_alice, "SENT---------->", " "], 
                    "public": [" ", " ", "PUBLIC INFO:", "a_n = " + a_n + ", b_n = " + b_n, " ", "a_e = " + a_e + ", b_e = " + b_e, " ", " ", " ", "PUBLIC: " + encrypted_alice, " "], 
                    "bob": ["BOB VARIABLES:", "b_p = " + b_p, "b_q = " + b_q, "b_n = b_p * b_q = " + b_n, "totient(b_n) = " + b_nt, "b_e = " + b_e, "b_d = " + b_d + " (from: 1 = b_e * b_d mod totient(b_n))", " ", " ", "RECIEVED: " + encrypted_alice, "DECRYPT (using m = c ^ b_d mod b_n): " + decrypt(encrypted_alice, int(b_d), int(b_n))]
                    }
        else:
            return "Can not send from Alice with an empty Alice Message field."
    # bob submit
    elif submitter == "1":
        if "bob_message" in parsed_form_data:
            bob_message = parsed_form_data["bob_message"][0]
            encrypted_bob = encrypt(bob_message, int(a_e), int(a_n))
            return {"alice": ["ALICE VARIABLES:", "a_p = " + a_p, "a_q = " + a_q, "a_n = a_p * a_q = " + a_n, "totient(a_n) = " + a_nt, "a_e = " + a_e, "a_d = " + a_d + " (from: 1 = a_e * a_d mod totient(a_n))", " ", " ", "RECIEVED: " + encrypted_bob, "DECRYPT (using m = c ^ a_d mod a_n): " + decrypt(encrypted_bob, int(a_d), int(a_n))], 
                    "public": [" ", " ", "PUBLIC INFO:", "a_n = " + a_n + ", b_n = " + b_n, " ", "a_e = " + a_e + ", b_e = " + b_e, " ", " ", " ", "PUBLIC: " + encrypted_bob, " "], 
                    "bob": ["BOB VARIABLES:", "b_p = " + b_p, "b_q = " + b_q, "b_n = b_p * b_q = " + b_n, "totient(b_n) = " + b_nt, "b_e = " + b_e, "b_d = " + b_d + " (from: 1 = b_e * b_d mod totient(b_n))", "SENDING: " + bob_message, "ENCRYPT (using c = m ^ a_e mod a_n): " + encrypted_bob, "<-------------SENT", " "]
                    }
        else:
            return "Can not send from Bob with an empty Bob Message field."
    return "ERROR"
