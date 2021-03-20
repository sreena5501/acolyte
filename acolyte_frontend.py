import tkinter as tk
from tkinter.constants import CENTER, COMMAND
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import acolyte_backend

root = tk. Tk()

root.resizable(True,True)

def textoutputed(a):
    text_box1.delete(1.0,50.0)
    text_box1.insert(1.0, a)

def textdetected(a):
    text_box.delete(1.0,50.0)
    text_box.insert(1.0,a)



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
browse_btn = tk.Button(root, textvariable=browse_text, bg="#3aa1c2",fg="white" ,font=("Magneto",'14'), command=lambda:acolyte_backend.start(), height=2,width=15,justify="center")
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

    
