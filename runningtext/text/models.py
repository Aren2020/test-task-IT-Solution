from django.db import models
from django.core.exceptions import ValidationError


def validate_video_extension(value):
    if not value.name.endswith(('.mp4')):
        raise ValidationError("Only video files are allowed.")

class Video(models.Model):
    text = models.CharField(max_length = 150)
    video = models.FileField(upload_to = 'video', validators = [validate_video_extension])
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.text

    class Meta:
        # For admin panel
        ordering = ['-created_at']
        indexes = [
            models.Index(fields = ['-created_at']),
        ]
