# Generated by Django 4.0.5 on 2022-09-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_posts_post_posts_summary_alter_posts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='home/pics-posts/default-post.png', upload_to='home/pics-posts'),
        ),
    ]
