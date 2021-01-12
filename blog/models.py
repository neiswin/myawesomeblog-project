from django.db import models

# Create your models here.

class Post(models.Model):
	blog_title = models.CharField(max_length = 50) 
	blog_date = models.DateTimeField()
	blog_text = models.CharField(max_length = 300) 
	blog_image = models.ImageField(upload_to = 'blog_images/')
 