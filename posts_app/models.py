from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # add in author and thumbnail later

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:60] + '...'