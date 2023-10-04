from django.db import models

# Create your models here.


class Details(models.Model):
    roll_number = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=10, null=True)


    def __str__(self): 
        return self.roll_number


class FullCollege(models.Model):
    roll_number = models.CharField(max_length=10, null=True)
    student_name = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.roll_number