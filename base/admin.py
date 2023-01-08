from django.contrib import admin
from .models import Report
# Register your models here.
# @admin.register(Sample)
# class SampleAdmin(admin.ModelAdmin):
# list_display = ['username','email']



@admin.register(Report)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['location1','location2','description','security','cause','action','type_env','type_inju','type_property','type_vehicle']