# Generated by Django 2.1.7 on 2020-06-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200608_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='programming.jpg', upload_to='blog_pics'),
        ),
    ]
