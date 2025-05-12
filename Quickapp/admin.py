from django.contrib import admin
from .models import Blog_Post, Category

# Register your models here.
admin.site.register(Blog_Post)
admin.site.register(Category)