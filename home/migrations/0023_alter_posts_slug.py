# Generated by Django 4.0.5 on 2022-10-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
