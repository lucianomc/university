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
    nameMatter = models.CharField(
        max_length=32, 
        help_text='Nome da Matéria')
    descriptionMatter = models.TextField(
        help_text='Uma breve descrição da ementa')
    numberStudent = models.IntegerField(
        help_text='O máximo de alunos por turma')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #student = models.ManyToManyField('Student', through='Student_has_matter')

    def __str__(self):
        return self.nameMatter


class Student(models.Model):
    idStudent = models.AutoField(primary_key=True)
    nameStudent = models.CharField(
        max_length=32, 
        help_text='Nome do Aluno')

    def __str__(self):
        return self.nameStudent


class Teacher(models.Model):
    idTeacher = models.AutoField(primary_key=True)
    nameTeacher = models.CharField(
        max_length=64, 
        help_text='Nome do Professor')
    matter = models.OneToOneField(
        Matter, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.nameTeacher

    # Como eu faço pra retornar só os campos de materia
    # depois que selecionar o curso?


# class Student_has_matter(models.Model):
#     note = models.DecimalField(max_digits=2, decimal_places=1)
#     teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
#     student = models.ForeignKey('Student', on_delete=models.CASCADE)
