from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

def Text_to_speech():
    if os.path.exists('TextSpeech.mp3'): # the below else condition takes the input and converts to speech,
        playsound('TextSpeech.mp3')      #buuuut.... if the user hits play again---this "if" is for that
    else:
        Message = entered_text.get()
        speech = gTTS(text = Message)
        speech.save('TextSpeech.mp3')
        playsound('TextSpeech.mp3')

def Reset():
    Msg.set('')
    os.remove('TextSpeech.mp3')

def Quit():
    if os.path.exists('TextSpeech.mp3'): # this is the normal "Exit" condition
        root.destroy()
    else:                   # this is incase if the user already hit the reset and then hits the Quit button
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
#to run the GUI+program
root.mainloop()
