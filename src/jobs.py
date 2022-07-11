import json
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify
from src.database import db, Skills
import requests

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED

job_post = Blueprint("jobs", __name__, url_prefix="/api/v1/jobs")


@job_post.get("/fetch")
def fetch_job(job_search: str, skill: str):

    if job_search == "":
        job_position = "data engineer"
    else:
        job_position = job_search.replace(" ", "%20")

    unfamiliar_skills = []

    if skill:
        _ = skill.split(",")
        for item in _:
            unfamiliar_skills.append((item.title()))

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

        return [
            data,
            (
                jsonify({"data": data}),
                HTTP_200_OK,
            ),
        ]


def add_skill(skills, job_title):
    """Insert skills and job title to the database

    Args:
        skills (list): list of dictionary
        job_title (str): job title inputted by the user

    Returns:
        json: returns a successful message after inserting the data
    """

    _ = []
    for skill in skills:
        for i in skill["skills"].split(","):
            for x in i.strip().split("/"):
                _.append(x.lower().strip())

    for i in _:
        save_skills = Skills(name=i, job_title=job_title)

        db.session.add(save_skills)
        db.session.commit()

    return jsonify({"message": "Data insert was successful!"}), HTTP_201_CREATED


# @job_post.get("/fetch_skills")
def get_skills():
    """Fetch the top 10 skills

    Returns:
        dict: 10 skills with the most count
    """

    skills_count = {}
    sorted_skills = {}

    skill_s = Skills.query.all()
    print(skill_s)

    for item in skill_s:
        # if item is in the dict, increment the value, if not set the value to 1
        # item was converted to string since sqlalchemy returns a diffent type
        skills_count[str(item)] = skills_count.get(str(item), 1) + 1

    # Sorting keys with the highest value
    sorted_keys = sorted(skills_count, key=skills_count.get, reverse=True)

    for i in sorted_keys:
        sorted_skills[i] = skills_count[i]

    # Only save the top 10 skills
    sorted_skills = dict(list(sorted_skills.items())[:10])

    return sorted_skills


def fetch_job_title(job_title: str):
    return job_title


def post_job_title():
    return fetch_job()
