from flask import Blueprint, render_template
from src.jobs import get_skills, get_job_title

dashboard = Blueprint("dashboard", __name__, url_prefix="/")


@dashboard.get("/dashboard")
def dash_page():

    skills = get_skills()
    dict_skills = skills
    # Convert the dictionary into a list with the sorted keys
    skills = sorted(skills)

    job_title = get_job_title().title()
    if job_title:
        return render_template("dashboard.html", skills=skills, job_title=job_title, dict_skills=dict_skills)
    else:
        return render_template("dashboard.html", skills=skills, job_title="Data Engineer (default)", dict_skills=dict_skills)