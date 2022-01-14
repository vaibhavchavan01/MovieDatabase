from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return super().__str__(self.name) 

class Movie(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    duration = models.DurationField()
    release = models.DateField()
    country = models.CharField(max_length=20)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class MovieArtist(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    artist  = models.ForeignKey(Artist, on_delete=models.CASCADE)
    a_type = models.CharField(max_length=20)
    def __str__(self) -> str:
        return super().__str__(self.a_type)

class User(AbstractBaseUser):
    
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=20, null= False, blank= False)
    confirm_password = models.CharField(max_length=20, null = False, blank= False)
    username = None
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    