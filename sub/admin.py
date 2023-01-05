import logging

from django.contrib import admin

# Register your models here.

from .models import Sub_log, TestModel

admin.site.register(Sub_log)
admin.site.register(TestModel)

