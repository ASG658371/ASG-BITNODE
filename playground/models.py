from django.db import models

# Create your models here.

class College (models.Model):

    college_id = models.BigAutoField(primary_key=True)
    college_name = models.CharField(max_length=200)

    def __str__(self):
        return self.college_name

class Subject (models.Model):

    subject_id = models.BigAutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name

class Student (models.Model):

    student_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.PositiveSmallIntegerField
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='studentts', blank=True)
