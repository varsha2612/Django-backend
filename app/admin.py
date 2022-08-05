from django.contrib import admin

# Register your models here.
from .models import guide, page, section
admin.site.register(guide)
admin.site.register(page)
admin.site.register(section)