# Generated by Django 2.2.5 on 2020-02-03 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0005_remove_question_not_before'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='optional_description',
        ),
    ]