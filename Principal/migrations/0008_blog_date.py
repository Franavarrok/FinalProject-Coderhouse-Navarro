# Generated by Django 4.1.7 on 2023-04-01 00:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0007_alter_blog_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
