# Generated by Django 3.1.6 on 2021-02-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0005_auto_20210214_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='chores',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
