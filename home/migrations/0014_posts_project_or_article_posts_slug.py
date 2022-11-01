# Generated by Django 4.0.5 on 2022-10-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_categories_project_or_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='project_or_article',
            field=models.CharField(choices=[('ART', 'Article'), ('PRJCT', 'Project')], default='ART', max_length=7),
        ),
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]