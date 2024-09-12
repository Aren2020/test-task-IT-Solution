from django.shortcuts import render
from django.urls import reverse
from .models import Video
from .forms import VideoForm
from .tasks import create_video_task

def create_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            text_content = form.cleaned_data['text']

            videos = Video.objects.filter(text = text_content)
            if videos.exists():
                # if text has already created we dont create the new one
                video = videos.first()
            else:
                video = form.save()
             
            create_video_task.delay(video.id)
            context = {'form': form, 'video_id': video.id} 
        else:
            context = {'form': form, 'error': 'Invalid input'}
    else:
        form = VideoForm()
        context = {'form': form}

    return render(request, 'text/index.html', context)