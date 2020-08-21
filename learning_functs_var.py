def function1():
    a = 5
    b = 6
    c = 5
    d = 6
    return a, b, c, d


def function2(var1, var2, var3, var4):
    print(var1, var2, var3, var4)


def run():
    a, b, c, d = function1()
    print(a, b, c, d)
    function2(a, b, c, d)


if __name__ == '__main__':
    run()