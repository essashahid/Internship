from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_subject_name(value):
    if not re.match("^[A-Za-z\s]+$", value):
        raise ValidationError("Subject name can only contain letters and spaces.")

class Subject(models.Model):
    name = models.CharField(max_length=100, validators=[validate_subject_name])

    def clean(self):
        # Custom model-level validation can be added here
        super().clean()

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
