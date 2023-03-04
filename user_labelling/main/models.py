from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Label(models.Model):
    # Label name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="label", null=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    