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
