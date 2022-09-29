from tracemalloc import start
from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from time import time

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
    start_date = models.IntegerField()
    end_date = models.IntegerField()

    # Status Enum
    class Status(Enum):
        ONGOING = 0
        UPCOMING = 1
        FINISHED = 2

    # Get status
    def get_status(self) -> Status:
        # Get the current time
        current_time = time.time()

        # If the start and end dates are 0, the contest is ongoing
        if start_date + end_date == 0:
            return self.Status.ONGOING
        
        # If the start date hasn't past, the contest hasn't started
        elif start_time > current_time:
            return self.Status.UPCOMING

        # If the end date has past, the contest has past
        elif end_time < current_time:
            return self.Status.FINISHED

        # If the start date has past, but the end date hasn't, the contest is ongoing
        elif start_time < time.time() and end_time > time.time():
            return self.Status.ONGOING