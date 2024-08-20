from django.contrib import admin
from django.urls import path, include
from home import views
from django.shortcuts import render

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