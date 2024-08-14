# Create your models here.
from django.db import models

class AIArtPhoto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ai_art/')

class MusicTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album_cover = models.ImageField(upload_to='album_covers/')
    listen_link = models.URLField()
    release_date = models.DateField()

class cardentry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    link = models.TextField(null=False, blank=False)
    featured_image = models.ImageField(upload_to='static/submitted', null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "card entries"
        ordering = ['-submit_date']

    def __str__(self):
        return self.title + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "card entries"
        ordering = ['-submit_date']
        
class Newsletter(models.Model):
    email = models.EmailField(unique=True, default='useremail@example.com')
    topic = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
    
    def __str__(self):
        return self.email
