from django.contrib import admin
from .models import Content

# register content model with admin dashboard.
admin.site.register(Content)
