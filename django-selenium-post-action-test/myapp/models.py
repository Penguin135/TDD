from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)])