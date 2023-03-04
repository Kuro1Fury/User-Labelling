from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Label, Item

admin.site.register(Label)
admin.site.register(Item)