from bs4 import BeautifulSoup
from flask import Blueprint, jsonify, request

jobs_post = Blueprint("jobs", __name__, url_prefix="/api/v1/jobs")
