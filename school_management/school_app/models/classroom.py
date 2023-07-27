from django.db import models
from .school_branch import SchoolBranch
from .subject import Subject
from .teacher import Teacher

class Classroom(models.Model):
    branch = models.ForeignKey(SchoolBranch, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.IntegerField()
    section = models.CharField(max_length=10)



class ClassroomSubjectTeacher(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classroom_subject_teachers')
