from django.core.exceptions import ValidationError
from django.db import models
from .classroom import Classroom
from .user_profile import UserProfile
import re

def validate_name(value):
    if not re.match("^[A-Za-z\s]+$", value):
        raise ValidationError("Name can only contain letters and spaces.")

class Student(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100, validators=[validate_name])
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
