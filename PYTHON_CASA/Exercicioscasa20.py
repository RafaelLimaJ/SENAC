a = 1
b = 1

def conta(a,b):
    for i in range(0, 10):
        print (b)
        reset = a
        a = b
        b = a + reset

conta(a,b)