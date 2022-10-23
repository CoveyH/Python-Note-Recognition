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