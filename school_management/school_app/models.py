from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=100)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class SchoolBranch(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    branch_manager = models.OneToOneField(User, on_delete=models.CASCADE)

class Classroom(models.Model):
    branch = models.ForeignKey(SchoolBranch, on_delete=models.CASCADE)
    grade = models.IntegerField()
    section = models.CharField(max_length=10)

class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class ClassroomSubjectTeacher(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
