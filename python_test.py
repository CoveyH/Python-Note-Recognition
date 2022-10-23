import random

a="a"
b="b"
c="c"
d="d"
e="e"
f="f"
g="g"

count = 0
note = [a,b,c,d,e,f,g]

test = random.sample(note, k=len(note))

def generate_notes():
    test = random.sample(note, k=len(note))

while True:
    if count == 7:
        generate_notes()
        count = 0
    for x in test:
        answered = False
        while answered == False:
            print ("What note is this: ", x)
            answer=input()
            if answer == x:
                print ("Correct!")
                count += 1
                answered == True
                break
            else:
                print("False")
                continue

import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("./g_note.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=-0.9, y=0.0)
root.mainloop()