# Generated by Django 4.1.7 on 2023-03-28 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Blogs'),
        ),
    ]
