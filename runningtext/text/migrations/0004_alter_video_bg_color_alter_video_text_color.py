# Generated by Django 5.1.1 on 2024-09-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_video_bg_color_video_duration_video_font_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='bg_color',
            field=models.CharField(default='#000000', help_text='Background color in hex (e.g., #000000 for black)', max_length=7),
        ),
        migrations.AlterField(
            model_name='video',
            name='text_color',
            field=models.CharField(default='#FFFFFF', help_text='Text color in hex (e.g., #FFFFFF for white)', max_length=7),
        ),
    ]
