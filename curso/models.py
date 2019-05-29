from django.db import models

# Create your models here.


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    nameCourse = models.CharField(max_length=45)
    descriptionCourse = models.TextField()

    def __str__(self):
       return self.nameCourse


# class Matter(models.Model):
#     idMatter = models.AutoField(primary_key=True)
#     nameMatter = models.CharField(max_length=32)
#     descriptionMatter = models.TextField()
#     numberStudent = models.IntegerField()
    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #teacher = models.ManyToManyField('Teacher', through='Matter_has_teacher')

    #def __str__(self):
    #    return self.nameMatter


# class Teacher(models.Model):
#     idTeacher = models.AutoField(primary_key=True)
#     nameTeacher = models.CharField(max_length=64)
    #matter = models.ManyToManyField('Matter', through='Matter_has_teacher')
    # Como eu faço pra retornar só os campos de materia depois que selecionar o curso?

    #def __str__(self):
    #    return self.nameTeacher


# class Matter_has_teacher(models.Model):
#     teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
#     matter = models.ForeignKey('Matter', on_delete=models.CASCADE)


# class Students(models.Model):
#     idStudent = models.AutoField(primary_key=True)
#     nameStudent = models.CharField(max_length=64)

#     def __str__(self):
#         return self.nameStudent


# class Student_has_matter(models.Model):
#     yieldStudent = models.DecimalField(max_digits=2, decimal_places=1)
#     student = models.ForeignKey('Students', on_delete=models.CASCADE)
#     matter = models.ForeignKey('Matter', on_delete=models.CASCADE)
