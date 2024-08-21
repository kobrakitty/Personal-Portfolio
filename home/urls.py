from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

# Titles for the backend platform
admin.site.site_header = "⚠️Portfolio Admin Page⚠️"
admin.site.site_title = "👽Back-end portal👽"

# Linking the views.py file to this one (urls.py)
urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('newsletter/', views.newsletter_form, name='newsletter_form'),
    path('generate-newsletter/', views.generate_newsletter, name='generate_newsletter'),
    path('subscribe/', views.subscribe, name='subscribe'),

]

# Serve media files during development and production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
