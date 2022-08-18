# Job skills scraper
## NOTE
   * Make sure to install the Python packages from the requirements.txt and generate the database file before running the Flask app.
   * This will scrape job postins from [Timesjobs](https://www.timesjobs.com).
      * Even though the website posts jobs for the Indian market, It think it's still relevant because it's the skills that I'm displaying.
## Overview
This is a basic web scraper for job postings. After fetching job posting/s based on the user input, the data (skills and job title) will be inserted to the database and display the top 10 skills in a dashboard.

Here is what each Python file (located under `src` directory) does:
* `__init__.py` - This is where the Flask/app config for the project are declared.
* `dashboard.py` - Function to render the template for the Dashboard page.
* `database.py` - Database structure for the project.
* `home.py` - Functions to render the template for the Home page.
* `jobs.py` - Functions to scrape for job posting, add and fetch skills from the database.
* `main.py` - Main file for running the app.
## Prerequisite
* Python
## How to run the scraper
Generate the database:
```
$ flask shell
$ from src.database import db
$ db.create_all()
```

Running the flask project:
```
$ flask run
```

On the `Home` page:
 * Input the desired job position that you want to search for.
    * If no input was submitted, the default job title is `Data engineer`.
 * Input all your unfamiliar skills in the 2nd textbox (comma separated)(``OPTIONAL``)

On the `Dashboard` page:
  * Displays the Top 10 skills for the searched job.
  * List out the Top 10 skills for the searched job.
## Helpful links
 * [Flask API tutorial](https://www.youtube.com/watch?v=WFzRy8KVcrM)
 * [Web scraping with Python](https://www.youtube.com/watch?v=XVv6mJpFOb0)
