from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(
        null=True, blank=True
    )  # null is for database to store no value entry&blank allows form to have empty value
