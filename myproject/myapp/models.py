from django.db import models


class MyApp(models.Model):
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_class = models.IntegerField()
    student_division = models.CharField(max_length=10)


