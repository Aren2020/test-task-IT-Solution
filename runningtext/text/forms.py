from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['text', 'width', 'height', 'duration', 'fps', 'font_size', 'text_color', 'bg_color']
        widgets = {
            'text_color': forms.TextInput(attrs = {'type': 'color'}),
            'bg_color': forms.TextInput(attrs = {'type': 'color'}),
        }