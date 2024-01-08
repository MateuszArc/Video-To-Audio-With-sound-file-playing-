#########################CONTANTS#########################
import subprocess
import os
import pygame

pygame.init()
#########################AUDIO MANAGING CLASS#########################
class Manage_Audio:
    def __init__(self):
        self.path = ""

    def convert_video_to_audio_ffmpeg(self, video_file, output_ext="mp3"):
        """Converts video to audio directly using `ffmpeg` command
        with the help of subprocess module"""
        
        filename, ext = os.path.splitext(video_file)
        self.path = filename+"."+output_ext
        subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        return self.path
    
    def play_sound(self, path:str, volume:float, loops:int):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops)

    

