from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoClip
from django.contrib.staticfiles import finders
from django.conf import settings
from dataclasses import dataclass
import numpy as np
import logging
import os

class VideoCreator:
    def __init__(
        self, video
    ):
        self.video = video
        self.font_path = finders.find('font/Alice-Regular.ttf')

        video_dir = os.path.join(settings.MEDIA_ROOT, 'video')
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
        
        self.video_save_path = os.path.join(video_dir, f'running_{self.video.text}.mp4')
        self.video_path = f'video/running_{self.video.text}.mp4'
        
    # Function to create a frame with text
    def make_frame(self, t):
        img = Image.new('RGB', (self.video.width, self.video.height), color = self.video.bg_color)
        draw = ImageDraw.Draw(img)

        # Font (you can specify the path to your font)
        font = ImageFont.truetype(self.font_path, self.video.font_size)

        # Calculate the size of the text using textbbox
        text_bbox = draw.textbbox((0, 0), self.video.text, font = font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Text position so it moves from right to left
        x = int(self.video.width - (t * (self.video.width + text_width) / self.video.duration) % (self.video.width + text_width))
        y = (self.video.height - text_height) // 2  # Centering vertically

        # Draw text
        draw.text((x, y), self.video.text, font = font, fill = self.video.text_color)

        # Convert image to numpy array for moviepy
        frame = np.array(img)
        return frame

    # Function to create video
    def create_video(self):
        try:
            # Use moviepy to create the video
            clip = VideoClip(lambda t: self.make_frame(t), duration = self.video.duration)
            clip = clip.set_fps(self.video.fps)

            logging.info("Starting video rendering...")
            clip.write_videofile(self.video_save_path, codec = "libx264")
            logging.info("Video successfully created!")

            return self.video_path
        except Exception as e:
            logging.error(f"An error occurred: {e}")
