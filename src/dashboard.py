from flask import Blueprint, render_template, request
from src.jobs import get_skills, get_job_title

dashboard = Blueprint("dashboard", __name__, url_prefix="/")


@dashboard.get("/dashboard")
def dash_page():

    skills = get_skills()
    # Convert the dictionary into a list with the sorted keys
    skills = sorted(skills)

    job_title = get_job_title().title()
    return render_template("dashboard.html", skills=skills, job_title=job_title)
