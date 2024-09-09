from django.db import models
from django.core.exceptions import ValidationError


def validate_video_extension(value):
    if not value.name.endswith(('.mp4')):
        raise ValidationError("Only video files are allowed.")

class Video(models.Model):
    text = models.CharField(max_length = 150)
    video = models.FileField(upload_to = 'video', validators = [validate_video_extension])
    width = models.PositiveIntegerField(default = 160)  # Default width (160px)
    height = models.PositiveIntegerField(default = 90)  # Default height (90px)
    duration = models.FloatField(default = 3)  # Default duration (3 seconds)
    fps = models.PositiveIntegerField(default = 30)  # Default FPS (30 fps)
    font_size = models.PositiveIntegerField(default = 30)  # Default font size (30)
    text_color = models.CharField(max_length = 7, default = '#FFFFFF')
    bg_color = models.CharField(max_length = 7, default = '#000000')
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.text

    class Meta:
        # For admin panel
        ordering = ['-created_at']
        indexes = [
            models.Index(fields = ['-created_at']),
        ]
