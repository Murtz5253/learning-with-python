# Generated by Django 4.1.3 on 2022-11-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0005_solution"),
    ]

    operations = [
        migrations.RemoveField(model_name="problem", name="id",),
        migrations.AddField(
            model_name="problem",
            name="problem_id",
            field=models.IntegerField(default=-1, primary_key=True, serialize=False),
        ),
    ]
