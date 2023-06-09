# Generated by Django 4.1.7 on 2023-03-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/Blogs'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
