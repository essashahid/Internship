from django.core.exceptions import ValidationError
import re
from django.db import models

def validate_school_name(value):
    if not re.match("^[A-Za-z\s]+$", value):
        raise ValidationError("School name can only contain letters and spaces.")

class School(models.Model):
    name = models.CharField(max_length=100, validators=[validate_school_name])
