import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Text to Speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#305065")

def exiting():
    sys.exit()

engine = pyttsx3.init()
def speakknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

#icon
image_icon = PhotoImage(file=resource_path("img\\speech.png"))
root.iconphoto(False, image_icon)

#Top frame
top_frame = Frame(root,bg="white",width=900,height=100)
top_frame.place(x=0,y=0)

logo2=Image.open(resource_path("img\\speech.png"))
logo2_resize = logo2.resize((90,90))
logo2_conver = ImageTk.PhotoImage(logo2_resize)
Label(top_frame,image=logo2_conver,bg="white").place(x=10,y=5)

Label(top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=120,y=30)

####
text_area = Text(root,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root, text='VOICE', font='arial 15 bold', bg="#305065",fg="white").place(x=580,y=160)
Label(root, text='SPEED', font='arial 15 bold', bg="#305065",fg="white").place(x=760,y=160)

gender_combobox = Combobox(root,values=['Male', 'Female'],font="arial 14", state='r', width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root,values=['Fast', 'Normal','Slow'],font="arial 14", state='r', width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

speak_image = Image.open(resource_path("img\\speak2.png"))
speak_resize = speak_image.resize((40,40))
speak_conver = ImageTk.PhotoImage(speak_resize)
btn = Button(root, text=" Speak",compound=LEFT,image=speak_conver,width=130,font="arial 14 bold",command=speakknow)
btn.place(x=547,y=280)

save_image = Image.open(resource_path("img\\save2.png"))
save_resize = save_image.resize((40,40))
save_conver = ImageTk.PhotoImage(save_resize)
save = Button(root, text=" Save",compound=LEFT,image=save_conver,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=727,y=280)


Label(root, text="Developed by Nipun Madhusankha",font="arial 8").place(x=720,y=422)

root.mainloop()
