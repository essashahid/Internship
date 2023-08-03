from django.core.exceptions import ValidationError
import re
from django.db import models
from .school_branch import SchoolBranch
from .subject import Subject
from .teacher import Teacher

def validate_section(value):
    if not re.match("^[A-Za-z0-9\s]+$", value):
        raise ValidationError("Section can only contain alphanumeric characters and spaces.")

def validate_grade(value):
    if value < 1 or value > 12:
        raise ValidationError("Grade must be between 1 and 12.")

class Classroom(models.Model):
    branch = models.ForeignKey(SchoolBranch, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.IntegerField(validators=[validate_grade])
    section = models.CharField(max_length=10, validators=[validate_section])

class ClassroomSubjectTeacher(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
