 #! /usr/bin/python

def p(width,height):
    for i in range(height):
        print("+-----"*width+"+")
        for j in range(height-2):
            print("|     "*height+"|")
    print("+-----"*width+"+")

p(5,5)

