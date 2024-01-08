#########################CONSTANTS#########################

from audio import Manage_Audio
import pygame
from tkinter import *
from tkinter import messagebox

pygame.init()

#########################APPLICATION#########################
if __name__ == "__main__":
    window = Tk()
    window.title("Wideo To Audio")
    window.config(padx=50,pady=50)    
    def play_sound():
        """
        play_sound function finds audio file in Audio Files and if it doesn't generate errors,
        plays it. Else it's raising .showerror() method 
        """
        global name_entry, extension_entry
        if name_entry.get() == "" or extension_entry.get() == "":
            messagebox.showerror(title="Wideo To Audio Error", message="Don't leave any fields empty!")
        else:
            pygame.display.set_icon(pygame.image.load(r'Icon.png'))#Modify this line: pygame.display.set_icon(pygame.image.load(r'Images\Icon.png')) if you want more sorted code
            pygame.display.set_caption("VideoToAudio.PlaySound")
            audio = Manage_Audio()
            try:
                audio.play_sound(r'{}.{}'.format(name_entry.get(), extension_entry.get()), 10.5, 1)#Modify this line: audio.play_sound(r'Audio Files\{}.{}'.format(name_entry.get(), extension_entry.get()), 10.5, 1) if you want more sorted code
                screen = pygame.display.set_mode((100, 100))
                screen.blit(pygame.image.load(r'Images\Icon.png'), (0, 0))
                pygame.display.update()
            except:
                messagebox.showerror(title="Wideo To Audio.Error",message="This file doesn't exist in workspace.")

    def convert():
        """This part is for converting file and adding it to main disc of user"""
        global name_entry, extension_entry, convert_extension_entry
        extension = convert_extension_entry.get()
        if extension == "wav" or extension == "mp3" or extension == "mkv" or extension == "MP4" or extension == "MOV" or extension == "AVI":
            audio = Manage_Audio()
            audio.convert_video_to_audio_ffmpeg(name_entry.get()+"."+extension_entry.get(),output_ext=extension)
            convert_extension_entry.delete(0,END)
    name_entry = Entry(width=35)
    name_entry.grid(column=1, row=1)
    extension_entry = Entry(width=35)
    extension_entry.grid(column=1, row=2)
    convert_extension_entry = Entry(width=35)
    convert_extension_entry.grid(column=2,row=3)

    playSoundButton = Button(text="Play File",command=play_sound)
    playSoundButton.grid(column=3,row=1)
    pauseSoundButton = Button(text="Pause File",command=pygame.mixer.music.pause)
    pauseSoundButton.grid(column=3,row=2)
    unpauseSoundButton = Button(text="Unpause File",command=pygame.mixer.music.unpause)
    unpauseSoundButton.grid(column=3,row=3)
    convertButton = Button(text="Convert to =>",command=convert)
    convertButton.grid(column=1,row=3)
    mainloop()