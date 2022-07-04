from flask import Blueprint, Flask, render_template, request

home = Blueprint("home", __name__, url_prefix="/")


@home.get("/")
def home_page():

    return render_template("home.html")


@home.route("/", methods=["POST", "GET"])
def fetch_input():
    """
    Retrieve the data from the job_post (name) input.
    """
    if request.method == "POST":
        default_value = 0
        data = request.form.get("job_post", default_value)
        print(f"Data: {data} | Type: {type(data)}")
    return render_template("home.html")
