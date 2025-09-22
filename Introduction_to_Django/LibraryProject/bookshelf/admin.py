from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'created_at')  
    search_fields = ('title',)                               
    list_filter = ('title',)                           
    ordering = ('-created_at',)
    
admin.site.register(Book)