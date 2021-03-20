import tkinter as tk
from tkinter.constants import CENTER, COMMAND
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from PyDictionary import PyDictionary
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import pyaudio

root = tk. Tk()

root.resizable(True,True)

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
dict = PyDictionary()

def textoutputed(a):
    text_box1.delete(1.0,50.0)
    text_box1.insert(1.0, a)

def textdetected(a):
    text_box.delete(1.0,50.0)
    text_box.insert(1.0,a)
    

def talk(text):
    textoutputed(text)
    rate=130
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def take_command(a):
    try:
        with sr.Microphone() as source:
            #print("input")
            listener.pause_threshold = 1
            voice = listener.listen(source,timeout=a,phrase_time_limit=a)
            #print("end")
            command=listener.recognize_google(voice)
            command=command.lower()
            textdetected(command)
            #print(command)
            return command
    except:
        talk("cant hear you, say again")
        return take_command(a)




def none(a):
    None
              
def meanin(key):
    try:
        x=(dict.meaning(key))
        z0=x.get('Verb')
        z1=x.get('Noun')
        z2=x.get('Adjective')

        i=""
        
        try:
            none(z0[0])
            n0=True
        except:
            n0=False
            
        try:
            none(z1[0])
            n1=True
        except:
            n1=False
        
        try:
            none(z2[0])
            n2=True
        except:
            n2=False
        
        

        num=0
        
        if n0==True:
            num=num+1
            i=i+"verb or"
        elif n1==True:
            num=num+1
            i=i+"noun or"
        elif n2==True:
            num=num+1
            i="adjective "
            
        #print (num)
        
        if num == 1:
            s=i
        elif num == 2:
            talk("you want "+i)
            s=take_command(4)        
        
            
        if "verb" in s:
            #print(z0[0])
            talk(z0[0])
        elif "noun" in s:
            #print(z1[0])
            talk(z1[0])
        elif "adjective" in s:
            #print(z2[0])
            talk(z2[0])
        else:     
            talk("cant get you")
            meanin(key)
    except:
        talk("meaning not available for "+key )
        
        
def syno(key):
    try:
        try:
            z=dict.synonym(key)
            #print (z[0]+" or "+z[1])
            talk(z[0]+" or "+z[1])
        except:
            #print(z[0])    
            talk(z[0])    
    except:
        talk("no synonym available")    
        
def anto(key): 
    try:
        try:
            z=dict.antonym(key)
            #print (z[0]+" or "+z[1])
            talk(z[0]+" or "+z[1])
            
        except:
            #print(z[0])
            talk(z[0])
    except:
        talk("no antonym available")       
    
def pron(key):
    b=""
    for i in key:
        if i==" ":
            None
            #print("space")
        else:
            b=b+i
    talk(b)
    #print(b)
    return 0

def spell(key):
    for i in range(len(key)):
        talk(key[i])
    

def song():
    playsound('song.mp3')
    
def start():

    #talk("hi I am your assistant you can ask me how to pronunce words or say meaning or synonym or antonym")
    talk("what u want me to do say meaning  synonym  antonym pronounciation or spelling ")
    choice=take_command(4)
    choice=choice.split()
    if "meaning" in choice:
        talk("say something")
        a=take_command(5)
        meanin(a)
        
    elif "synonym" in choice:
        talk("say something")
        a=take_command(5)
        syno(a)
        
    elif "antonym" in choice:
        talk("say something")
        a=take_command(5)
        anto(a)
        
    elif "pronunciation" in choice or "pronunce" in choice:
        talk("say something")
        a=take_command(7)
        pron(a)
        
    elif "music" in choice:
        song()

    elif "spelling" in choice:
        talk("say something")
        a=take_command(5)
        spell(a)
        
    elif "stop" in choice:
        return 0

    else:
        talk("cant get you")
        return 0


canvas = tk.Canvas(root, width=0, height=170, bg="white") 
canvas.grid(columnspan=9, rowspan=5)
root.title('Acolyte') 
root.resizable(height = True, width=True)

#logo
logo = Image.open('logo1.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo,justify="center")
logo_label.image = logo
logo_label.grid(column=4, row=1)

#instructions

instructions = tk.Label(root, text="commands available: \n Meaning \n Synonym \n Antonym \n pronunciation \n spelling \n music \n stop", font=("Harrington",'14','bold'), bg="#3aa1c2",fg="white",justify="left")
instructions.grid( rowspan=4,column=7, row=1)

#button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, bg="#3aa1c2",fg="white" ,font=("Magneto",'14'), command=lambda:start(), height=2,width=15,justify="center")
browse_text.set("Click to Start")
browse_btn.grid(column=0, row=1)

canvas= tk.Canvas (root, width=680, height=210, bg="#3aa1c2")#20bebe")
canvas.grid(columnspan=9,rowspan=5)


instructions = tk.Label(root, text="TEXT OUTPUTED", font=("CentSchbkCyrill BT",'12'), bg="#3aa1c2",fg="black",justify="center")
instructions.grid( rowspan=3,column=0, row=5)


instructions = tk.Label(root, text="TEXT DETECED", font=("CentSchbkCyrill BT",'12'), bg="#3aa1c2",fg="black",justify="center")
instructions.grid( rowspan=3,column=7, row=5)

    
instructions = tk.Label(root, text="White Hat team present's", font=("Brush Script MT",'22'), bg="#3aa1c2",fg="black",justify="center")
instructions.grid( columnspan=3,column=3, row=9,ipadx=2)

text_box1 = tk.Text(root, height=3, width=25)
#text_box.tag_configure("center", justify="center") text_box.tag_add("center", 1.0, "end")
text_box1.grid(rowspan=3,column=0, row=6)


text_box = tk.Text(root, height=3, width=25)
#text_box.tag_configure("center", justify="center") text_box.tag_add("center", 1.0, "end")
text_box.grid(rowspan=3,column=7, row=6)
#talk("hi I am your assistant you can ask me how to pronunce words or say meaning or synonym or antonym")
    

root.mainloop()
