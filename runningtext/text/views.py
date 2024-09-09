from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from .utils import VideoCreator

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
                video = form.save(commit = False)
                video_creator = VideoCreator(video)
                video_url = video_creator.create_video()
                video.video = video_url
                video.save()

            context = {'form': form, 'video': video}
        else:
            context = {'form': form, 'error': 'Invalid input'}
    else:
        form = VideoForm()
        context = {'form': form}

    return render(request, 'text/index.html', context)