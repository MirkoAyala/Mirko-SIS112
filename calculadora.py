int =print("ingrse un numero ")
def suma(a,b):
    return  a+b 

def resta(a,b):
    return a-b

def multiplicación(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "error de division"
    return a/b

def calculator():
    print("Seleccione operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    