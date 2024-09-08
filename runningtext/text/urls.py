from django.urls import path
from . import views

app_name = 'text'

urlpatterns = [
    path('video/', views.create_video, name = 'create_video'),
]