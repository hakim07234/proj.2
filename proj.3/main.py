from re import L
from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox

root = Tk()
root.title('Employee Qrcode[Rakwan]')
root.geometry('370x470+500+100')
root.resizable(False,False)

#def welcome():
   # music = AudioSegment.from_mp3('sounds/welcome1.mp3')
   # play(music)

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voice',voices[1].id)

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

def TakeCommands():
    command= sr.Recognizer()
    with sr.Microphone() as mic:
        command.phrase_threshold= 0.1
        audio = command.listen(mic)
        try:
            query = command.recognize_google(audio, language='ar')
        except Exception as Error:
            print(Error)
        return query.lower()

def b1():
    query = TakeCommands()
    name = query
    E1.insert(0,name)
def b2():
    query = TakeCommands()
    name = query
    E2.insert(0,name)
def b3():
    query = TakeCommands()
    name = query
    E3.insert(0,name)
def Sv():
    namefile = En_save.get()
    name = E1.get()
    co   = E2.get()
    job  = E3.get()
    info = qrcode.make(name + co + job)
    info.save('employee/'+namefile+'.jpg')
    messagebox.showinfo('Save','Save [' +namefile+ '] employee')



photo = PhotoImage(file='logo.png')
l_img = Label(root, image=photo)
l_img.place(x=2,y=1,width=365,height=200)

l = Label(root, text='Emp Name :',font=('Tajawal',14))
l.place(x=10,y=230)

l1 = Label(root, text='Country :',font=('Tajawal',14))
l1.place(x=10,y=270)

l2 = Label(root, text='Emp Job :',font=('Tajawal',14))
l2.place(x=10,y=310)

E1 = Entry(root,font=('Tajawal',14))
E1.place(x=130,y=230)

E2 = Entry(root,font=('Tajawal',14))
E2.place(x=130,y=270)

E3 = Entry(root,font=('Tajawal',14))
E3.place(x=130,y=310)

b1=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b1)
b1.place(x=340,y=230)

b2=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b2)
b2.place(x=340,y=270)

b3=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b3)
b3.place(x=340,y=310)


l_save = Label(root, text='File Save :',font=('Tajawal',14))
l_save.place(x=10,y=382)
En_save= Entry(root,font=('Tajawal',16),width=11)
En_save.place(x=137,y=380)
b_save=Button(root,text='Save ✅',fg='white',bg='red',font=('Tajawal',11),command=Sv)
b_save.place(x=286,y=378)

l_copy =Label(root,text='Devloper hakim',font=('Tajawal',14))
l_copy.place(x=130,y=435)


#welcome()
root.mainloop()


