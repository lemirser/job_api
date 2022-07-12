from src.jobs import del_skills_data, fetch_job, add_skill
from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint("home", __name__, url_prefix="/")


@home.get("/")
def home_page():

    return render_template("home.html", result=0)


@home.post("/")
def fetch_input():
    """
    Delete the skills data and retrieve the data from the job_post (name) input.
    """
    del_skills_data()

    if request.method == "POST":
        job_search = request.form.get("job_post")
        skill = request.form.get("skills", "")

        result = fetch_job(job_search, skill)

        if result[0]:

            add_skill(result[0], job_search)

            return redirect(url_for("dashboard.dash_page"))

        else:
            return render_template("home.html", result=1)


@home.post("/home")
def redirect_home():
    """Delete skills data when the user tried to search for a new job.

    Returns:
        template: Renders the home.html
    """
    del_skills_data()
    return render_template("home.html", result=0)
