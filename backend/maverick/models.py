from django.contrib.auth.models import User
from django.db import models

class MaverickUser(User):
    featured_image = models.ImageField(default = "default.png")
    about = models.TextField(blank=True)