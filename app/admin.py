from django.contrib import admin
from app import models
admin.site.register(models.News)
admin.site.register(models.Category)
admin.site.register(models.Tags)
# Register your models here.
