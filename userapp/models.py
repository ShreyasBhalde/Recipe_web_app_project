from django.db import models

# Create your models here.


class profile(models.Model):
    username = models.CharField(max_length=35,primary_key=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    number = models.CharField(max_length=12)

    class Meta:
        db_table = "profile"
        