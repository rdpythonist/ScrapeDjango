import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ScraperDjango.settings")
app = Celery("ScraperDjango")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
