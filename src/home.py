from src.jobs import fetch_job
from flask import Blueprint, render_template, request

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
        return fetch_job(job_search, skill)
    return home_page()
