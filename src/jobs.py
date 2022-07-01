import json
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify, request
import requests

from src.constants.http_status_codes import HTTP_200_OK

job_post = Blueprint("jobs", __name__, url_prefix="/api/v1/jobs")


@job_post.get("/fetch")
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

    data = []

    if job_posts:
        for job_post in job_posts:
            publish_date = job_post.find("span", class_="sim-posted")

            # Only include jobs that were posted few days ago from the current day
            if "few" in publish_date.text.strip():
                # Fetch all company name in the webpage that are under the "job"
                company_name = job_post.find("h3", class_="joblist-comp-name").text.replace("(More Jobs)", "").strip()

                skills = job_post.find("span", class_="srp-skills").text.strip()

                # Fetch the link for the job posting.
                job_posting = job_post.header.h2.a["href"]

                # Cleans all incorrectly formatted "skills"
                temp_skills = skills.split(",")
                _ = []
                for skill in temp_skills:
                    _.append(skill.strip().replace("  ", " ").replace(" ,", ",").title())

                    skills = ", ".join(_)

                unfamiliar_skills = []
                if any(
                    unfamiliar_skill in skills for unfamiliar_skill in unfamiliar_skills
                ):  # Don't include job post with unfamiliar skill
                    # If the unfamiliar skill is in "skills", it will skip it because that's how "continue" works
                    continue
                # If the condition is true, skip/ do not display the result and start again with the condition.

                data.append(
                    {
                        "company": company_name.title(),
                        "skills": skills,
                        "url": job_posting,
                    },
                )

        return (
            jsonify({"data": data}),
            HTTP_200_OK,
        )
        # print(post_details)


if __name__ == "__main__":
    fetch_job()
