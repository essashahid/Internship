from django.db import models
from .user_profile import UserProfile
from django.core.exceptions import ValidationError
import re

def validate_name(value):
    if not re.match("^[a-zA-Z\s]*$", value):
        raise ValidationError("Name should only contain letters and spaces.")

class Teacher(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE,related_name='teachers')
    name = models.CharField(max_length=100, validators=[validate_name])
