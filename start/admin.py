from django.contrib import admin

from .models import Charge

# Register your models here.
# 在 127.0.0.1/admin/ 可看到database
admin.site.register(Charge)