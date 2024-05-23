# Generated by Django 5.0.3 on 2024-05-22 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='educational_state',
            fields=[
                ('User', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(default=None, max_length=200)),
                ('Schools', models.CharField(default=None, max_length=200)),
                ('Faculty', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('University', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]
