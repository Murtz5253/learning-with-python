# Generated by Django 4.1.3 on 2022-11-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0003_question_question_code"),
    ]

    operations = [
        migrations.RenameModel(old_name="Question", new_name="Problem",),
        migrations.RenameField(
            model_name="problem", old_name="question_code", new_name="problem_code",
        ),
    ]
