from django.db import models
from django.contrib.auth.models import User


class Main_contents(models.Model):
    name = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255, )
    description = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    s_dt = models.DateTimeField(blank=True, null=True)
    e_dt = models.DateTimeField(blank=True, null=True)
    descript = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Headliner(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    job = models.ForeignKey("Position",
                            on_delete=models.CASCADE,
                            )


class Position(models.Model):
    name = models.CharField(max_length=245)
