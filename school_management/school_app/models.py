from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=100)


class SchoolBranch(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)


class Classroom(models.Model):
    branch = models.ForeignKey(SchoolBranch, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.IntegerField()
    section = models.CharField(max_length=10)


class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)


class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)


class ClassroomSubjectTeacher(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classroom_subject_teachers')


class UserSchoolBranch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_school_branches')
    school_branch = models.ForeignKey(SchoolBranch, on_delete=models.CASCADE, related_name='user_school_branches')
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('BRANCH_MANAGER', 'Branch Manager'),
        # add more roles if needed
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
