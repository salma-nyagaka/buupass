# Generated by Django 3.1.6 on 2021-02-13 19:15

import buupass.helpers.fancy_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chores',
            fields=[
                ('id', models.CharField(db_index=True, default=buupass.helpers.fancy_generator.fancy_id_generator, editable=False, max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.TextField(max_length=300)),
                ('completed', models.BooleanField(default=False)),
                ('date_completed', models.DateTimeField(verbose_name='date completed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
