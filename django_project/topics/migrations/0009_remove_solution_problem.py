# Generated by Django 4.1.3 on 2022-12-01 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0008_alter_solution_problem"),
    ]

    operations = [
        migrations.RemoveField(model_name="solution", name="problem",),
    ]