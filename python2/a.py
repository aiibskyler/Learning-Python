
def multi(args):
    args=eval(args)
    result = 1
    for e in args:
        result = result * e
    return result

x = (input("请输入数字："))
print(multi(x))


def p(size):
    for i in range(size):
        print("+--------" * size + "+")
        print("|        " * size + "|")
        print("|        " * size + "|")
        print("|        " * size + "|")
        print("|        " * size + "|")
        print("|        " * size + "|")
    print("+--------" * size + "+")

p(5)
