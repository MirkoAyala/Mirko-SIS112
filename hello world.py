n = int(input("ingrese un numero").strip())
if n % 2 == 1:
            print("Weird")
else:
    if n>=2:
        if n<=5:
            print ("Not Weird")
        elif n>=6:
            if n<=20:
                print("Weird")
            elif n>20:
                print ("Not Weird")
a = int(input("ingrese un numero "))
b = int(input("ingrese otro numero "))
    
suma= a+b
diferencia=a-b
producto=a*b
print(suma)
print(diferencia)
print(producto)

a = int(input())
b = int(input())
print(a//b)
print(a/b)


if _name_ == '_main_':
    n = int(input())
    if n<=20:
        for i in range(n):
            print(i**2)
    else:
        print("no esta en el rango permitido")