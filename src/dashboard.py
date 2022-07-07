from flask import Blueprint, render_template, request
from src.jobs import get_skills

dashboard = Blueprint("dashboard", __name__, url_prefix="/")


@dashboard.get("/dashboard")
def dash_page():

    skills = get_skills()
    return render_template("dashboard.html", skills=skills)
