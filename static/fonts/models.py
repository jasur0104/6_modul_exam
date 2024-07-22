from django.db import models
class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

# Create your models here.
