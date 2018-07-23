import datetime
def move(n,a,b,c):
    if n==1:
        pass
        #print(a,'->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
# start = datetime.time()
# move(64,'A','B','C')
# end = datetime.time()
#
# print (end-start)
a = int(input("请输入步数"))
year = ((2**a-1)/86400)/365
print("第{}层汉诺塔需要移动{}步,如果一步需要1秒钟，那么需要{}年".format(a,2**a-1,year))
