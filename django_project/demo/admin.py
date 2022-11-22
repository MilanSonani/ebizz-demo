from django.contrib import admin
from .models import Tag, Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_completed')
    search_fields = ('name',)

admin.site.register(Todo, TodoAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'bgcolor', 'color')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
