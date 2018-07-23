# coding=UTF-8
from random import randint
x = randint(0, 300)
for count in range(0,5):
    print ('Please input a number between 0~300:')
digit = int(input())
if digit == x :
    print ('Bingo!')
elif digit > x:
    print ('Too large,please try again.')
else:
    print ('Too small,please try again.')