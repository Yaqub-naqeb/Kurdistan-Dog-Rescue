from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    picture = models.ImageField(null=True, blank=True, default='default.png', upload_to='dog_pictures/')
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name