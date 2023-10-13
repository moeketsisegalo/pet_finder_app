from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pet_finder_app/pet_images/', null=True, blank=True)

    def __str__(self):
        return self.name

