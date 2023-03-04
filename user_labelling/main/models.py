from django.db import models

# Create your models here.
class Label(models.Model):
    # Label name
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text