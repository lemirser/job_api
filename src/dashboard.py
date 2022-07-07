from flask import Blueprint, render_template, request

dashboard = Blueprint("dashboard", __name__, url_prefix="/")


@dashboard.get("/dashboard")
def dash_page():
    return render_template("dashboard.html")
