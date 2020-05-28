from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model


class User(AbstractUser):
  pass


class Company(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    companyName = models.CharField(max_length=255, null=True)
    companyDescription = models.TextField(null=True)
    symbol = models.CharField(max_length=5, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField(max_length=4, blank=True, null=True)
    low_high = models.CharField(max_length=255, blank=True, null=True)
    marketCap = models.IntegerField(blank=True, null=True)
    ytdChange = models.FloatField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.symbol
