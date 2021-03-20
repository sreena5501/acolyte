import random
from PyDictionary import PyDictionary
import speech_recognition as sr
import pyttsx3
from playsound import playsound
import acolyte_frontend

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
dict = PyDictionary()



def talk(text):
    acolyte_frontend.textoutputed(text)
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
            acolyte_frontend.textdetected(command)
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
    talk("what u want me to do say meaning  synonym  antonym or pronounciation  ")
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
        
    elif "spelling" in choice or "spell" in choice:
        talk("say something")
        a=take_command(5)
        spell(a)
    
    elif "stop" in choice:
        return 0

    else:
        talk("cant get you")
        return 0

