from flask import Blueprint, Flask, render_template

home = Blueprint("home", __name__, url_prefix="/")


@home.get("/")
def home_page():
    return render_template("home.html")
