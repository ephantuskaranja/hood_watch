from django.contrib import admin
from .models import Hood, Recommendation, Reports
# Register your models here.
admin.site.register(Hood)
admin.site.register(Recommendation)
admin.site.register(Reports)