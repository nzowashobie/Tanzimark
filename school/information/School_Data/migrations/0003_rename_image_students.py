# Generated by Django 4.1.1 on 2022-10-15 11:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School_Data', '0002_image_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Students',
        ),
    ]