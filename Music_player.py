import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('Music Player')
root.geometry('400x480')
pygame.mixer.init()

list_of_songs = ['music/Nas - Represent.mp3', 'music/Loose Ends - Ooh You Make Me Feel.mp3', 'music/Loose Ends - Gonna Make You Mine.mp3']
list_of_covers = ['img/Illmatic Album Artwork.jpg', 'img/Loose Ends - Tighten Up Vol 1 1992 Front.jpg', 'img/00 - Loose Ends - The Best of (2003).jpg']

n = 0 

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((250,250))
    load = ImageTk.PhotoImage(image2)

    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=0.19, rely=0.09)

    stripped_string = song_name[6:-3]
    song_name_label = tkinter.Label(text=stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=0.35,rely=0.62)
                            


def update_progress_bar():
    if pygame.mixer.music.get_busy():
        current_pos = pygame.mixer.music.get_pos() / 1000  # Get position in seconds
        progress_bar.set(current_pos / song_len)
        root.after(1000, update_progress_bar)  # Schedule the next update in 1 second

def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    global song_len
    song_len = a.get_length()  # Get length of song in seconds
    progress_bar.configure(maximum=song_len)  # Set the maximum value of the progress bar to the length of the song
    update_progress_bar()  # Start the recursive updating of the progress bar


# def progress():
#     a = pygame.mixer.Sound(f'{list_of_songs[n]}')
#     song_len = a.get_length() * 3
#     for i in range(0, math.ceil(song_len)):
#         time.sleep(.4)
#         progress_bar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progress, daemon=True)
    t1.start()

def play_music():
    threading()
    global n
    current_song = n
    if n > 3:
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    get_album_cover(song_name, n)
        

    print('PLAY')
    n += 1

def skip_forward():
    pass

def skip_back():
    global n
    n -= 3
    play_music() 

def volume(value):
    pygame.mixer.music.set_volume(value)


# Buttons

play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_forward = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_forward.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)

skip_back = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_back.place(relx=0.29, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210 )
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progress_bar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progress_bar.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)






root.mainloop()
