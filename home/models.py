# Create your models here.
from django.db import models 
from django.conf import settings


class cardentry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    link = models.TextField(null=False, blank=False)
    featured_image = models.ImageField(upload_to='uploads/explore/', null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "card entries"
        ordering = ['-submit_date']
        
class gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    link = models.TextField(null=False, blank=False)
    featured_image = models.ImageField(upload_to='uploads/gallery/', null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "gallery"
        ordering = ['-submit_date']
        
class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    link = models.TextField(null=False, blank=False)
    featured_image = models.ImageField(upload_to='uploads/project/', null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "project"
        ordering = ['-submit_date']
    
    def get_image_url(self):
        if self.featured_image:
            return f"{settings.MEDIA_URL}{self.featured_image}"
        return ""
                
class Newsletter(models.Model):
    email = models.EmailField(unique=True, default='useremail@example.com')
    topic = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
    
    def __str__(self):
        return self.email
