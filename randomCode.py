#! /usr/bin/python
import random
for i in range(10):
    list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    code = random.sample(list,8)
    print("密码：","".join(code))

