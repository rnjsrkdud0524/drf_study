from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complete', 'important', 'created')
    search_fields = ('title', 'description')
    list_filter = ('complete', 'important')
    ordering = ('-created',)

    fields = ('title', 'description', 'complete', 'important')