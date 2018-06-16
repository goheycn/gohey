from django.contrib import admin
from . import models
from goheys.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)

# Register your models here.
