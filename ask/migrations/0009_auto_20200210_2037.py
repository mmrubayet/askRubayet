# Generated by Django 2.2.5 on 2020-02-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20200206_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]