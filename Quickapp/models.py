from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Blog_Post(models.Model):

    options =(
            ('draft', 'Draft'),
            ('published', 'Published'),
    )
    
    image = models.ImageField(upload_to= 'img/', null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True )
    slug = models.SlugField(unique=True, blank=True)

    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now =True)
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)
        super().save(*args, **kwargs)