# Generated by Django 2.1.7 on 2020-06-11 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200608_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Post')),
            ],
        ),
    ]
