# apps/profiles/models.py
from django.db import models
from django.conf import settings


class Profile(models.Model):
    ROLE_CHOICES = [
        ("investor", "Investor"),
        ("founder", "Founder"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="investor")
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email