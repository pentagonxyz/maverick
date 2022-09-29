from django.contrib.auth.models import User
from django.db import models
from enum import Enum

# User Model
class MaverickUser(User):
    # Profile Picture
    featured_image = models.ImageField(default = "default.png")
    about = models.TextField(blank=True)

# Challenge Model
class Challenge(models.Model):
    # Problem title
    title = models.CharField(max_length=200)

    # Problem description
    description = models.TextField(max_length=1000,blank=True)

    # Starting + Ending Dates (time.time())
    # If both == 0, challenge is constant
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
