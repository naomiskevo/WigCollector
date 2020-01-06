from django.contrib import admin
from .models import Wig, Condition, Photo

# Register your models here.
admin.site.register(Wig)
admin.site.register(Condition)
admin.site.register(Photo)