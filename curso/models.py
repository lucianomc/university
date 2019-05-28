from django.db import models

# Create your models here.


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    nameCourse = models.CharField(max_length=45)
    descriptionCourse = models.TextField()

    def __str__(self):
        return self.nameCourse


class Matter(models.Model):
    idMatter = models.AutoField(primary_key=True)
    nameMatter = models.CharField(max_length=32)
    descriptionMatter = models.TextField()
    numberStudent = models.IntegerField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameMatter
