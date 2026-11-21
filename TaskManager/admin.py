from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links=['title', 'id']
    search_fields = ['title', 'id', 'caption']
    list_filter = ['user_id', 'id']

