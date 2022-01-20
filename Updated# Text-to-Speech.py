from tkinter import *
from gtts import gTTS
from pygame import mixer
import os

def Text_to_speech():
    
    if len(Msg.get()) != 0:
        
        if os.path.exists('TextSpeech.mp3'):
            mixer.quit()
            os.remove('TextSpeech.mp3')

        Message = entered_text.get()
        speech = gTTS(text = Message)
        speech.save('TextSpeech.mp3')
        
        mixer.init()
        mixer.music.load('TextSpeech.mp3')
        mixer.music.play()

    else:
        print('Please Enter Something in the text box')
        root.mainloop()

def Reset():
    Msg.set('')
    mixer.quit()
    if os.path.exists('Textspeech.mp3'):
        os.remove('TextSpeech.mp3')
    
def Quit():
    root.destroy()
    
def on_closing():
    root.destroy()

#The GUI declaration and the decoration
root = Tk()
root.geometry('600x300')
root.resizable(0,0)
root.config(bg = '#D4D4CA')
root.title('Text to Speech Engine')
Label(root, text = 'Text to Speech Engine' , font='Helvettica 20 bold' , bg ='#D4D4CA').pack()

# The Input Sector
Label(root, text ='Enter Text', font ='Helvettica 18 bold', bg ='#D4D4CA').place(x=60,y=60)
Msg = StringVar()
entered_text = Entry(root,textvariable =Msg, width ='50')
entered_text.place(x=20 , y=100)

#All Buttons
Button(root, text = 'Play ►' , font = 'Helvettica 15 bold', command = Text_to_speech, width =6, bg='green').place(x=330, y=90)
Button(root, text = 'Reset ╬', font='Helvettica 15 bold', command = Reset, bg='yellow').place(x=420, y =90)
Button(root,text = 'Quit',font = 'Helvettica 15 bold' , command = Quit, bg = 'Dark red').place(x=420,y=160)
# the icons beside 'Play' and 'Reset', got those from Character map-windows

