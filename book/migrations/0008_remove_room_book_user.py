# Generated by Django 3.2.7 on 2022-05-20 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_user_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_book',
            name='user',
        ),
    ]