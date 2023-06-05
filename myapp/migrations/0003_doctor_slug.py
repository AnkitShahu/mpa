# Generated by Django 4.2.1 on 2023-06-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(default=' ', max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
    ]