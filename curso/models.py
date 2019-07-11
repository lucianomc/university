from django.db import models

# Create your models here.


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    nameCourse = models.CharField(max_length=45)
    descriptionCourse = models.TextField()

    def __str__(self):
        return self.nameCourse

# E o UUIDField


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
    students = models.ManyToManyField('Student', through='StudentHasMatter')

    def __str__(self):
        return self.nameMatter
        # return f'{self.nameMatter} ({self.course})'


class Teacher(models.Model):
    idTeacher = models.AutoField(primary_key=True)
    nameTeacher = models.CharField(
        max_length=64,
        help_text='Nome do Professor')
    matter = models.OneToOneField(
        Matter,
        on_delete=models.CASCADE)
    # Poderia usar models.SET_NULL?

    def __str__(self):
        return self.nameTeacher

    # Como eu faço pra retornar só os campos de materia
    # depois que selecionar o curso?


class Student(models.Model):
    idStudent = models.AutoField(primary_key=True)
    nameStudent = models.CharField(
        max_length=32,
        help_text='Nome do Aluno')

    def __str__(self):
        return self.nameStudent


class StudentHasMatter(models.Model):
    note = models.DecimalField(max_digits=2, decimal_places=1)
    matter = models.ForeignKey('Matter', on_delete=models.DO_NOTHING)
    student = models.ForeignKey('Student', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.student}"

    def note(self):
        return self.note
