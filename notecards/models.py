from django.db import models
from leads.models import Lead

# Create your models here.

class Notecards(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=600)
  # owner = models.ForeignKey(Lead, on_delete=models.CASCADE)
