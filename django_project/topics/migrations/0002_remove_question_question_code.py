# Generated by Django 4.1.3 on 2022-11-22 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="question", name="question_code",),
    ]
