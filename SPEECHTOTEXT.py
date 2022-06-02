#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sounddevice as sd
from tkinter import *
from tkinter.ttk import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
from datetime import datetime


def threading_rec(x):
    if x == 1:
        t1 = threading.Thread(target=record_audio())
        t1.start()
    elif x == 2:
        global recording
        recording = False
        messagebox.showinfo(message="Recording finished")

def callback(indata, frames, time, status):
    q.put(indata.copy())


def record_audio():
    global recording
    recording = True
    global file_exists
    messagebox.showinfo(message="Recording Audio. Speak into the mic")
    name_of_file =  datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    with sf.SoundFile("Nasila_"+ name_of_file+".wav", mode='w', samplerate=44100, channels=2) as file:
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording == True:
               file_exists =True
               file.write(q.get())


voice_rec = Tk()
voice_rec.geometry("200x150")
voice_rec.title("Voice Recorder")
voice_rec.config(bg="#248f8f")

style = Style()

style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'red')], background=[('active', 'black')])
q = queue.Queue()

recording = False
file_exists = False

title_lbl = Label(voice_rec, text="", background="#107dc2")
record_btn = Button(voice_rec, text="Start Recording", command=lambda m=1: threading_rec(m))
record_btn.pack(pady=30)

stop_btn = Button(voice_rec, text="Stop Recording", command=lambda m=2: threading_rec(m))
stop_btn.pack(pady=3)

voice_rec.lift()
voice_rec.attributes('-topmost', True)
voice_rec.after_idle(voice_rec.attributes, '-topmost', False)

voice_rec.mainloop()




