from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Race)
admin.site.register(Calendar)
admin.site.register(User)
