# Generated by Django 4.2.13 on 2024-05-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furumapp', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=False, upload_to='images'),
            preserve_default=False,
        ),
    ]