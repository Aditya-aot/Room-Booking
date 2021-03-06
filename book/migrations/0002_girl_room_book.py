# Generated by Django 3.2.7 on 2022-05-23 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='girl_room_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a101', models.BooleanField(default=False, verbose_name='101')),
                ('a102', models.BooleanField(default=False, verbose_name='102')),
                ('a103', models.BooleanField(default=False, verbose_name='103')),
                ('a104', models.BooleanField(default=False, verbose_name='104')),
                ('a105', models.BooleanField(default=False, verbose_name='105')),
                ('a106', models.BooleanField(default=False, verbose_name='106')),
                ('a107', models.BooleanField(default=False, verbose_name='107')),
                ('a108', models.BooleanField(default=False, verbose_name='108')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
