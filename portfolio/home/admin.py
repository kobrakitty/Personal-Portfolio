from django.contrib import admin
from .models import cardentry, Newsletter, gallery, project
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Register your models here.
admin.site.register(cardentry)
admin.site.register(gallery)
admin.site.register(project)

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        subject = f"Newsletter on {newsletter.topic}"
        context = {
            'subject': newsletter.topic,
            'message': newsletter.content
        }
        html_content = render_to_string('newsletter_email.html', context)
        email = EmailMessage(
            subject,
            body=html_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[],
            bcc=['shelbywentz@gmail.com', 'tyler.kd.knapp@gmail.com']  # Update this to the list of recipients
        )
        email.content_subtype = 'html'  # This is required because we need to send HTML content
        email.send()

send_newsletter.short_description = "Send selected newsletters via email"

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_at')
    actions = [send_newsletter]
admin.site.register(Newsletter, NewsletterAdmin)
