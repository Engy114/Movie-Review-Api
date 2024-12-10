from django.db import models
from .serializers import ReviewSerializer

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Review(models.Model):
    movie_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movie {self.movie_id} - {self.rating}"
