from django.db import models

# Create your models here.


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    nameCourse = models.CharField(max_length=45)
    descriptionCourse = models.TextField()

    def __str__(self):
        return self.nameCourse
