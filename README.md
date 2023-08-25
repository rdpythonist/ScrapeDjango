Django REST Project for Scraping Google Play Store Data
This project uses Django REST framework to scrape data from the Google Play Store. The following steps are involved:

Scrape the data from the URL https://play.google.com/store/games?hl=en&gl=US.
Filter out the package names from the scraped data.
Fetch the package details from the Play Store for each package name.
Store the data in a database.
Use Celery and Redis to queue the tasks for fetching package details.
Requirements
Python 3
Django
Django REST framework
Google Play Scraper
Celery
redis
Installation
Create a virtual environment and activate it.
Install the requirements:
pip install -r requirements.txt


3. Create a new Django project:

django-admin startproject myproject

4. Create app :
python manage.py startapp 'app_name'
Add the google-play-scraper and celery packages to the INSTALLED_APPS setting in myproject/settings.py:
INSTALLED_APPS = [
...
'app',
'rest_framework',
]

6. Start Redis server:
redis-server
5. Create a new celery worker:

celery -A ScraperDjango.celery worker -l info


6. Run the Django development server:

python manage.py runserver

Usage
The project provides a simple API for fetching data from playstore url. To get started, make a request to the following endpoint:

POST /app/appdetails
Example:{
    "url":"https://play.google.com/store/games?hl=en&gl=US"
}

This will return a list of all the apps that have been scraped from the google_scraper library one by one in queue using celery. To get more information about a specific app, make a request to the following endpoint:

GET /app/applist

responsed_data= [{
        {
            "id": 239,
            "title": "RAID: Shadow Legends",
            "rating": 1940826,
            "genre": "Role Playing",
            "score": "4.5558"
        },
        {
            "id": 240,
            "title": "Top Eleven Be a Soccer Manager",
            "rating": 6442082,
            "genre": "Sports",
            "score": "4.5625"
        }]