# Generated by Django 4.0.3 on 2022-06-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consaltations',
            name='Photo',
            field=models.FileField(blank=True, upload_to='consultation_image/'),
        ),
    ]
