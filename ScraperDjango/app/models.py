from django.db import models

# Create your models here.
class AppDetails(models.Model):
    title=models.CharField(max_length=80)
    rating=models.PositiveIntegerField()
    genre=models.CharField(max_length=50)
    score=models.DecimalField(max_digits=10,decimal_places=4)


    def __str__(self):
        return self.title