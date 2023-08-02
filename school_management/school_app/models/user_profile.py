from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import re

def validate_role_choice(value):
    valid_choices = [UserProfile.SCHOOL_ADMIN, UserProfile.SCHOOL_BRANCH_MANAGER]
    if value not in valid_choices and value is not None:
        raise ValidationError(f"Invalid role choice: {value}")

class UserProfile(models.Model):
    user = models.OneToOneField(User, db_index=True, related_name='profile', on_delete=models.CASCADE)
    SCHOOL_ADMIN = 'ADMIN'
    SCHOOL_BRANCH_MANAGER = 'BRANCH_MANAGER'
    SCHOOL_ROLE_CHOICES = (
        (SCHOOL_ADMIN, "Admin"),
        (SCHOOL_BRANCH_MANAGER, "Branch Manager"),
    )
    role = models.CharField(max_length=20, choices=SCHOOL_ROLE_CHOICES, null=True, blank=True, default=None, validators=[validate_role_choice])

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
