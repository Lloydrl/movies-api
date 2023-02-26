from django.db import models

class MovieData(models.Model):

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=200, default='romantic comedy')
    image = models.ImageField(upload_to='images/', default='images/none/noimg.jpg')

    def __str__(self):
        return self.name
