from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoClip
from django.contrib.staticfiles import finders
from django.conf import settings
from .models import Video
import numpy as np
import logging
import os

class VideoCreator:
    def __init__(
        self, text, font_size = 30,
        width = 160, height = 90, 
        duration = 3, fps = 30,
        text_color = (255, 255, 255), bg_color = (0, 0, 0) 
    ):
        # Video parameters
        self.width = width
        self.height = height # Increased resolution for better text quality
        self.text = text
        self.duration = duration # Length of video in seconds
        self.fps = fps # Frames per second
        self.font_size = font_size # Increased font size
        self.text_color = text_color # White text color
        self.bg_color = bg_color # Black background
        self.font_path = finders.find('font/Alice-Regular.ttf')

        video_dir = os.path.join(settings.MEDIA_ROOT, 'video')
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
        
        self.video_save_path = os.path.join(video_dir, f'running_{self.text}.mp4')
        self.video_path = f'video/running_{self.text}.mp4'
        
    # Function to create a frame with text
    def make_frame(self, t):
        img = Image.new('RGB', (self.width, self.height), color = self.bg_color)
        draw = ImageDraw.Draw(img)

        # Font (you can specify the path to your font)
        font = ImageFont.truetype(self.font_path, self.font_size)

        # Calculate the size of the text using textbbox
        text_bbox = draw.textbbox((0, 0), self.text, font = font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Text position so it moves from right to left
        x = int(self.width - (t * (self.width + text_width) / self.duration) % (self.width + text_width))
        y = (self.height - text_height) // 2  # Centering vertically

        # Draw text
        draw.text((x, y), self.text, font = font, fill = self.text_color)

        # Convert image to numpy array for moviepy
        frame = np.array(img)
        return frame

    # Function to create video
    def create_video(self):
        try:
            # if text has already created
            videos = Video.objects.filter(text = self.text)
            if videos.exists():
                return videos.first()

            # Use moviepy to create the video
            clip = VideoClip(lambda t: self.make_frame(t), duration = self.duration)
            clip = clip.set_fps(self.fps)

            logging.info("Starting video rendering...")
            clip.write_videofile(self.video_save_path, codec = "libx264")
            video = self.save_in_db()     
            logging.info("Video successfully created!")

            return video
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def save_in_db(self):
        return Video.objects.create(
            text = self.text,
            video = self.video_path  
        )