from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Laundry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothCount = models.IntegerField()
    reg_number = models.CharField(max_length=10)
    date = models.DateField(null=True, auto_now=True)
    out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reg_number} - {self.clothCount} - {self.date}"
