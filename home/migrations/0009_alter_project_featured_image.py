# Generated by Django 5.1 on 2024-08-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_cardentry_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/project/'),
        ),
    ]
