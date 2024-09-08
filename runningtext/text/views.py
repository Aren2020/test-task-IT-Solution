from django.shortcuts import render
from .forms import TextForm
from .utils import VideoCreator

def create_video(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text_content = form.cleaned_data['text']
            video_creator = VideoCreator(text_content)
            video = video_creator.create_video()  # Assuming this method returns the path of the created video
            context = {'form': form, 'text': text_content, 'video_url': video.video.url}
        else:
            context = {'form': form, 'error': 'Invalid input'}
    else:
        form = TextForm()
        context = {'form': form}

    return render(request, 'text/index.html', context)