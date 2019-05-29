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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameMatter


# class Teacher(models.Model):
#     idTeacher = models.AutoField(primary_key=True)
#     nameTeacher = models.CharField(max_length=64)

    # Como eu faço pra retornar só os campos de materia depois que selecionar o curso?

    #def __str__(self):
    #    return self.nameTeacher
