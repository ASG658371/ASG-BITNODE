from django.db import models

# Create your models here.

class Colleges (models.Model):
    colleges_id = models.BigAutoField(primary_key=True)
    colleges_name = models.CharField(max_length=200)
class Subjects (models.Model):
    subjects_id = models.BigAutoField(primary_key=True)
    subjects_name = models.CharField(max_length=200)
class Students (models.Model):
    students_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.PositiveSmallIntegerField
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    colleges_id = models.ForeignKey(Colleges, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subjects, related_name='studentts', blank=True)
