# apps/projects/models.py

from django.db import models
from django.conf import settings


class Project(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("active", "Active"),
        ("funded", "Funded"),
        ("closed", "Closed"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# apps/projects/models.py (add below)

class Investment(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="investments")
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} → {self.project}"