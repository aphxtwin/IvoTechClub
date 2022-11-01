# Generated by Django 4.0.5 on 2022-09-30 14:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='summary',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
