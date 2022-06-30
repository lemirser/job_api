from bs4 import BeautifulSoup
from flask import Blueprint, jsonify, request
import requests

# job_post = Blueprint("jobs", __name__, url_prefix="/api/v1/jobs")


# @job_post.get("/fetch")
def fetch_job():
    job_position = "data+engineer"
    html_text = requests.get(
        # .text will not display the RESPONSE code from the website
        f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_position}&txtLocation="
    ).text

    soup = BeautifulSoup(html_text, "lxml")

    job = soup.find("li", class_="clearfix job-bx wht-shd-bx")

    print(job.text)


if __name__ == "__main__":
    fetch_job()
