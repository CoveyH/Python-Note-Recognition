import random


a="a"
b="b"
c="c"
d="d"
e="e"
f="f"
g="g"

note = [a,b,c,d,e,f,g]


question = False

while True:

    test = random.sample(note, k=len(note))

    for x in test:
        print ("What note is this: ", x)
        answer=input()
        if answer == x:
            print ("True")
            continue
        else:
            print("False")
            question = False
            break
        