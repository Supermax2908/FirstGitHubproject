# Generated by Django 5.0.3 on 2024-03-24 08:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.SET_NULL, related_name='post', to=settings.AUTH_USER_MODEL),
            preserve_default='False',
        ),
    ]
