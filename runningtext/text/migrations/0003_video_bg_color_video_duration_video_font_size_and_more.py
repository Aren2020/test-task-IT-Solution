# Generated by Django 5.1.1 on 2024-09-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_video_delete_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='bg_color',
            field=models.JSONField(default=(0, 0, 0), help_text='Background color in RGB format'),
        ),
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.FloatField(default=3, help_text='Duration of the video in seconds'),
        ),
        migrations.AddField(
            model_name='video',
            name='font_size',
            field=models.PositiveIntegerField(default=30, help_text='Font size of the text'),
        ),
        migrations.AddField(
            model_name='video',
            name='fps',
            field=models.PositiveIntegerField(default=30, help_text='Frames per second'),
        ),
        migrations.AddField(
            model_name='video',
            name='height',
            field=models.PositiveIntegerField(default=90),
        ),
        migrations.AddField(
            model_name='video',
            name='text_color',
            field=models.JSONField(default=(255, 255, 255), help_text='Text color in RGB format'),
        ),
        migrations.AddField(
            model_name='video',
            name='width',
            field=models.PositiveIntegerField(default=160),
        ),
    ]
