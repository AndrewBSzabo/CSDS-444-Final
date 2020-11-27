# CSDS-444-Final

Caeser Cipher (enc0),
Vigenere Cipher (enc1),
DES (enc2),
RSA (enc3),
MD 5 checksum (enc4)


To run application:
1. cd into CSDS-444-Final/

2. Create a virtualenv (and activate it):

python3 -m venv venv

. venv/bin/activate

3. Install the flask app:

pip install -e .

4. Run the server:

export FLASK_APP=comp_sec

export FLASK_ENV=development


For Windows:
set FLASK_APP=comp_sec
set FLASK_ENV=development

flask run

5. Go to http://127.0.0.1:5000/ in browser
