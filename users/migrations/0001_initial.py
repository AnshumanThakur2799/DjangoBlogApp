# Generated by Django 5.0.4 on 2024-04-09 14:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
