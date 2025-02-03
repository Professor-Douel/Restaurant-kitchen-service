from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.username} ({self.years_of_experience} років досвіду)"
