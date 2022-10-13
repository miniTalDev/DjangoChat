# Generated by Django 4.1.2 on 2022-10-10 00:29

import chat.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_usersetting_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersetting',
            name='profile_image',
            field=models.ImageField(blank=True, default='\\profile-pics\\default.jpg', null=True, upload_to=chat.models.random_file_name),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
