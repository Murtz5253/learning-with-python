# Generated by Django 4.1.3 on 2022-12-11 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0017_alter_problem_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="problem", name="user",),
    ]
