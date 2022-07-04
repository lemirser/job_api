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
        default_value = "data engineer"
        job_search = request.form.get("job_post", default_value)
        skill = request.form.get("skills", "")
        print(f"Data: {job_search} | Type: {type(job_search)}")
        print(f"Data: {skill} | Type: {type(skill)}")
    return render_template("home.html")
