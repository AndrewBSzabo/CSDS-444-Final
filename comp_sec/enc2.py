from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort


bp = Blueprint("enc2", __name__, url_prefix="/enc2")


@bp.route("/")
def index():
    """Redirects to buy page, users are not allowed to access the index"""
    return "enc2 page"
    return redirect(url_for("trade.buy"))


# @bp.route("/read/<int:id>", methods=("GET",))
# def read(id):
#     """Shows all reviews + ratings for a specific user"""
#     db = get_db()
#     posts = db.execute(
#         # todo: make query
#     ).fetchall()
#     return render_template("review/read.html", posts=posts)
#
#
# @bp.route("/write/<int:id>", methods=("GET", "POST"))
# def write(id):
#     """Allows a user to write a review for a specific meal swipe"""
#     # if the form is submitted, process it
#     if request.method == "POST":
#         # todo: change everything within if
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None
#
#         if not title:
#             error = "Title is required."
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
#                 (title, body, g.user["id"]),
#             )
#             db.commit()
#             # todo: add reviewee user id to redirect
#             return redirect(url_for("review.read"))
#
#     # if user is not submitting form, display page
#     return render_template("review/write.html")