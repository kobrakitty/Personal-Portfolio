# Generated by Django 5.1 on 2024-08-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(default='useremail@example.com', max_length=254, unique=True),
        ),
    ]
