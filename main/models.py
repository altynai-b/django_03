from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    desctiption = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"