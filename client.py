
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


window=Tk()
window.title('music Window')
window.geomectory("300*300")
window.configure(bg='LightSkyBlue')






for file in os.listdir('shared_files'):
    filename=os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter= song_counter+1

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    pygame 
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected !=""):
        INFOlabel.configure(text="now playing"+song_selected)
    else:
        INFOlabel.configure(text="")

PLAYButton=Button(window,text="Play",bd=1, font = ("Calibri",10), )
PLAYButton.place(x=200,y=200)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
ResumeButton=Button(window,text="Resume",bd=1, font = ("Calibri",10))
ResumeButton.place(x=30,y=250)


def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
PauseButton=Button(window,text="Pause",bd=1, font = ("Calibri",10))
PauseButton.place(x=200,y=250)






def stop():
    global song_selected
    pygame 
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    INFOlabel.configure(text="")
    
Stop=Button(window,text="Stop",bd=1, font = ("Calibri",10))
Stop.place(x=30,y=200)




selectlabel1 = Label(window, text= "Enter a song", font = ("Calibri",10))
selectlabel1.place(x=2, y=1)

listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
listbox.place(x=10, y=10)

scrollbar1 = Scrollbar(listbox)
scrollbar1.place(relheight = 1,relx = 1)
scrollbar1.config(command = listbox.yview)

Stop=Button(window,text="Stop",bd=1, font = ("Calibri",10))
Stop.place(x=30,y=200)

PLAYButton=Button(window,text="Play",bd=1, font = ("Calibri",10), )
PLAYButton.place(x=200,y=200)
    
Download=Button(window,text="Download",bd=1, font = ("Calibri",10))
Download.place(x=30,y=250)

Upload=Button(window,text="Upload",bd=1, font = ("Calibri",10))
Upload.place(x=200,y=250)

ResumeButton=Button(window,text="Resume",bd=1, font = ("Calibri",10))
ResumeButton.place(x=30,y=250)

PauseButton=Button(window,text="Pause",bd=1, font = ("Calibri",10))
PauseButton.place(x=200,y=250)

INFOlabelLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
INFOLabel.place(x=10, y=330)

window.mainloop()



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

musicWindow()
setup()


























