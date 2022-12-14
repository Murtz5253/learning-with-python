# Learning With Python
A web application to help introductory learners with Python.

## Mission
Learning With Python's mission is to provide introductory Python learners with an outlet to practice their Python skills and receive comprehensive feedback on their overall performance and mastery metrics. At a higher level, our mission is to further research in computer science education, specifically in the area of studying student misconceptions in introductory programming.

## Overview
This software tool was designed and implemented in connection with research at the Learning and Design Lab in Human-Centered Design and Engineering at the University of Washington. It pertains to the niche research field of concept inventories in computer science, under the larger research umbrella of computer science education.

A concept inventory (CI) is a standardized set of questions which can be used to measure student understanding of core concepts within a discipline. The primary advantage of concept inventories–as compared with traditional assessments–is that beyond just identifying concepts students are struggling with, they can help to pinpoint the specific misconceptions that students hold. The idea of concept inventories first emerged in 1998, when Hestenes, Wells, and Swackhamer published the Force Concept Inventory (FCI), widely known as the original concept inventory as well as the gold standard within the field. This concept inventory focuses on the principles of Newtonian Force, identified as a crucial concept for introductory physics students. The authors were inspired to develop this tool in light of research which had revealed that introductory physics students across the United States held misconceptions about how force worked based on everyday common sense, and that conventional methods for physics instruction at the time failed to bring about any meaningful change in these beliefs.

In recent years, computer science education researchers have made efforts toward the development of concept inventories in their own field. This tool related most directly to research coming out of The State University of Campinas, where researchers led by [Ricardo Caceffo](https://www.ricardocaceffo.com/) have made progress toward building [concept inventories for introductory programming in various languages](https://www.ricardocaceffo.com/concept-inventory).

This tool attempts to build on this work by providing a usable tool with a repository of some of the existing concept inventory questions in Python. The tool is still under development, and the final goal is to develop a way to extract student misconceptions from free-form questions, as concept inventories are currently limited to a multiple-choice format.

## Repository Structure

## Installation Instructions
Learning with Python is designed to be installed from the command line. Using a virtual environment is recommended, as there are many required dependencies (we provide an environment.yml file to streamline your setup process). Detailed directions are provided below.

1. Open your terminal (we recommend Terminal for MacOS and [Ubuntu 20.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab) for Windows).
2. Clone the repoistory at https://github.com/Murtz5253/learning-with-python
3. Enter into the newly formed learning-with-python directory with `cd learning-with-python`.
4. Set up a new virtual environment with all necessary packages and dependencies using `conda env create -f environment.yml`
5. Activate the virtual environment with `conda activate lwp`
6. The virtual environment must remain active throughout your usage of the Learning With Python tool (see below for Usage details). Once you have finished, you can deactivate the virtual environment using `conda deactivate`

## Usage
There are two separate use cases for the tool in its current state, as all aspects of the intended algorithm for analyzing student data have not yet been integrated. We outline directions for each of the two use cases below.

### The Web Application
1. Ensure your virtual environment is activated as per the directions above.
2. The web application is configured to run with a PostgreSQL database, which should have been installed as part of the virtual environment. However, you will still need to set up and configure the database before the web application can be used. Start by entering the PostgreSQL command prompt by typing in the command `psql`.
3. Run the following commands in order to set up your database as per the project requirements (you can change the username and password if you wish; we just provide examples that can be easily referenced): `CREATE DATABASE central;`, `CREATE USER lwp WITH PASSWORD 'Hyku78^'`, `ALTER ROLE lwp SET client_encoding TO 'utf8';`, `ALTER ROLE lwp SET default_translation_isolation TO 'read committed';`, `ALTER ROLE lwp SET timezone TO 'UTC';`, `GRANT ALL PRIVILEGES ON DATABASE central TO lwp;`. These steps will set up the database to work with the Django web application.
4. Exit the PostGreSQL prompt.
5. Activate the database connection from your terminal. If you are running Linux, the command is `sudo pg_ctlcluster 12 main start`.
6. Navigate to the outermost `django_project` directory in the project. To confirm that you are in the correct directory, run `ls` and ensure you see a file called `manage.py`.
7. Run the following command to load initial data needed for the web application into the database: `python manage.py loaddata initial_data.json`.
8. Start the server with the commanf `python manage.py runserver`. You should see a web application running at the specified port! You can navigate around the page and try out a few things.
9. The following steps outline specific use cases that you may be interested in testing out.
10. We have generated example student progress visualizations with toy data to demonstrate what this tool will look like when fully functioning. To test this out, you can register as an example student using the Register button in the top right. Ensure the username is "student1." The email and password can be whatever you wish, but the password must meet complexity requirements or the program will throw an error. After registering, sign in as this student, and go to "View Progress" to see some data pertaining to this student. You can try this with other usernames as well: "student2," "student3," and "student4."
11. While logged in as a student, you can also go to the Problems page, and try editing and submitting code for various problems (currently, we just have sample problems with toy code). After you submit, you should find your respective solutions on the Solutions page. Submitted solutions are unique to the user logged in at a given time.
### The Data Analysis

## Acknowledgments

Many thanks to David Beck and Erin Wilson for guiding us through this project!

