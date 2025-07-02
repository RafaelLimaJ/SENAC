a = 1
b = 1

def conta(a,b):
    for i in range(0, 10):
        reset = a
        a = reset
        a = b
        b = a + b
        print (a)

conta(a,b)