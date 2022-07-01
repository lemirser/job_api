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

    # Initialize BeautifulSoup
    soup = BeautifulSoup(html_text, "lxml")

    # Fetch job list
    job_posts = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    if job_posts:
        for job_post in job_posts:
            publish_date = job_post.find("span", class_="sim-posted")

            # Only include jobs that were posted few days ago from the current day
            if "few" in publish_date.text.strip():
                # Fetch all company name in the webpage that are under the "job"
                company_name = job_post.find("h3", class_="joblist-comp-name").text.replace("(More Jobs)", "").strip()

                skills = job_post.find("span", class_="srp-skills").text.strip()


if __name__ == "__main__":
    fetch_job()
