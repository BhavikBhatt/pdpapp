from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=40)
    post = models.ForeignKey(Post, related_name="comments")

    def __str__(self):
        return self.text

class State(models.Model):
    name = models.CharField(max_length=40)
    numpdp = models.IntegerField()
    cost = models.FloatField()

    def __str__(self):
        return self.name


