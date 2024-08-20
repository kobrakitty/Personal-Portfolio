
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import cardentry, Newsletter, gallery, project
from django.contrib import messages
from django.conf import settings
from openai import OpenAI
from django.db import IntegrityError
from openai import OpenAI
import os
from dotenv import load_dotenv

# Set OpenAI API key
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
OPENAI_API_KEY = "sk-proj-MdAO5GToPAILjmIPmqXFT3BlbkFJVKCK82et7F8JKc4ozqWF"

# Create your views here
#New card entries make sure there is a matching template
def home(request):
    card_entries = cardentry.objects.all().order_by('-submit_date')
    # Fetch gallery entries from the gallery model
    gallery_entries = gallery.objects.all().order_by('-submit_date')
    project_entries = project.objects.all().order_by('-submit_date')

    # Prepare the context with the model data
    gallery_data = [{'url': entry.featured_image.url, 'title': entry.title, 'description': entry.description} for entry in gallery_entries]
    project_data = [{'url': entry.featured_image.url, 'title': entry.title, 'description': entry.description} for entry in project_entries]
    
    context = {
        'entries': card_entries,
        'gallery_entries': gallery_data,
        'project_entries': project_data
    }
    
    return render(request, 'home.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                # Create a new Newsletter entry
                Newsletter.objects.create(email=email)
                messages.success(request, 'You have successfully subscribed!')
            except IntegrityError:
                messages.error(request, 'This email is already subscribed, yay!')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
            return redirect('home')  # Redirect to the home page or wherever you prefer
    return render(request, 'home.html')  # Ensure you have a fallback to render the template

def submit(request):
    entries = cardentry.objects.all().order_by('-submit_date')
    context = {'entries': entries}

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        featured_image = None

        if 'featured_image' in request.FILES:
            featured_image = request.FILES['featured_image']
        else:
            pass

        new_entry = cardentry(title=title, description=description, link=link, featured_image=featured_image)
        new_entry.save()


        return redirect('home')
    else:
        return render(request, 'submit.html', context)
    
def submit(request):
    entries = gallery.objects.all().order_by('-submit_date')
    context = {'entries': entries}

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        featured_image = None

        if 'featured_image' in request.FILES:
            featured_image = request.FILES['featured_image']
        else:
            pass

        new_entry = gallery(title=title, description=description, link=link, featured_image=featured_image)
        new_entry.save()

        return redirect('home')
    else:
        return render(request, 'submit.html', context)

def newsletter_form(request):
    return render(request, 'newsletter_form.html')

def generate_newsletter(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        # Read the API key
        api_key = settings.OPENAI_API_KEY

        # Initialize the OpenAI client
        client = OpenAI(api_key=api_key)
        messages = [
            {"role": "system", "content": "You are a newsletter writing whiz. You write brief, helpful newsletters about topics. Your newsletters are brief but insightful and often use lots of emojis. You always start the newsletter with Hello! and end you newsletter with Have a Great Day!"},
            {"role": "user", "content": f"Please write a detailed newsletter about {topic}."}
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )

        content = response.choices[0].message.content

        # Save the generated newsletter to the database
        Newsletter.objects.create(topic=topic, content=content)

        return render(request, 'generated_newsletter.html', {'topic': topic, 'content': content})

    return redirect('newsletter_form')

def new_page(request):
    return render(request, 'music.html')