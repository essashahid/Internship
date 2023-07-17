from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile', on_delete=models.CASCADE)
    SCHOOL_ADMIN = 'ADMIN'
    SCHOOL_BRANCH_MANAGER = 'BRANCH_MANAGER'
    SCHOOL_ROLE_CHOICES = (
        (SCHOOL_ADMIN, "Admin"),
        (SCHOOL_BRANCH_MANAGER, "Branch Manager"),
    )
    role = models.CharField(max_length=20, choices=SCHOOL_ROLE_CHOICES, null=True, blank=True, default=None)

class School(models.Model):
    name = models.CharField(max_length=100)

class SchoolBranch(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(UserProfile, blank=True, related_name='admin_school_branches')
    branch_managers = models.ManyToManyField(UserProfile, blank=True, related_name='manager_school_branches')

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
