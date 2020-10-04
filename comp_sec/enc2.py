from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

bp = Blueprint("enc2", __name__, url_prefix="/enc2")


@bp.route("/")
def index():
    """Redirects to buy page, users are not allowed to access the index"""
    return "enc2 page"