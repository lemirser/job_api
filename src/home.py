from src.jobs import fetch_job, add_skill
from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint("home", __name__, url_prefix="/")


@home.get("/")
def home_page():

    return render_template("home.html")


@home.post("/")
def fetch_input():
    """
    Retrieve the data from the job_post (name) input.
    """
    if request.method == "POST":
        job_search = request.form.get("job_post")
        skill = request.form.get("skills", "")

        result = fetch_job(job_search, skill)

        add_skill(result[0], job_search)

    return redirect(url_for("dashboard.dash_page"))
