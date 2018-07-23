Cash = input("请输入带符号的现金额\n")
if Cash[-1] in ['$']:
    rmb = (eval(Cash[0:-1])/6.27)
    print("{:.2f}￥".format(rmb))
elif Cash[-1] in ['￥']:
    dollar = (eval(Cash[0:-1])*6.27)
    print('{:.2f}$'.format(dollar))
else:
    print("输入错误！")