# Generated by Django 4.1.7 on 2023-03-28 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
