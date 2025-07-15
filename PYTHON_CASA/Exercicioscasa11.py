Num1 = int(input("Primeiro Numero?"))
Num2 = int(input("Segundo Numero?"))
Num3 = int(input("Terceiro Numero?"))
check1 = 0
check2 = 0
check3 = 0
if Num1 > Num2:
    check1 = check1 + 1
elif Num1 > Num3:
    check1 = check1 + 1
if Num2 > Num3:
    check2 = check2 + 1 
elif Num2 > Num1:
    check2 = check2 + 1
if Num3 > Num1:
    check3 = check3 + 1 
elif Num3 > Num2:
    check3 = check3 + 1
if check1 == 2:
    print(f"O {Num1} é o maior numero!")
if check2 == 2:
    print(f"O {Num2} é o maior numero!")
if check3 == 2:
    print(f"O {Num3} é o maior numero!")