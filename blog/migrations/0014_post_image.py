# Generated by Django 2.1.7 on 2020-06-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200607_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='programming.jpg', upload_to='blog_pics'),
        ),
    ]
