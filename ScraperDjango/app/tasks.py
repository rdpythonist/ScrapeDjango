from time import sleep
from celery import shared_task
from google_play_scraper import app
from .models import AppDetails

# Task for fetching and saving package data in DB
@shared_task(bind=True)
def get_details(self,package_names):
    my_dict={}
    for packages in package_names:
        try:
            result = app(
                packages,
                lang='en', # defaults to 'en'
                country='us' # defaults to 'us'
            )
            my_dict={"title":result['title'],
                            'genre':result['genre'],
                            'rating':result['ratings'],
                            'score':result['score']}
            AppDetails.objects.create(**my_dict)  #Save details in DB one by one using celery task
        except Exception as e:
            pass
    return True