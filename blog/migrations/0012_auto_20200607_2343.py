# Generated by Django 2.1.7 on 2020-06-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200604_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
