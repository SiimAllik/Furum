# Generated by Django 5.0.6 on 2024-05-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furumapp', '0003_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(max_length=100),
        ),
    ]
