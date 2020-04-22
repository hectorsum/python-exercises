#x = 10 # esto es un comentario
#print(x)
#x ="Hola mundo"
#print(x,"cruel")
x = 0
if x>0:
    print("positivo")
    print("ultra positivo")
    print("mas que positivo")
else:
    if x<0:
        print("negativo")
        print("ultra negativo")
    else:
        print("valor cero")
 
mascotas = ["gato","perro","loro","guepardo"]
#for m in mascotas:
#    print(m)
#for i in range(len(mascotas)):
#    print((i+1),".-",mascotas[i])
#for i in range(2,10,3):# for(int i = 2;i<10;i+=3)
#    print(i)
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def potencia(a,b):
    return a**b

x = int(input("ingrese primer valor: ")) # int("5")  5
y = int(input("ingrese segundo valor: "))
print("La suma es:",sumar(x,y))
print("La resta es:",restar(x,y))
print("La potencia es:",potencia(x,y))
#------------------------
x = int(input("ingrese primer valor: ")) # int("5")  5
y = int(input("ingrese segundo valor: "))# int("15")  15
z = int(input("ingrese tercer valor: "))# int("8")  8

# retornarme x 5  es el menor
# retornarme y 15 es el mayor
# retornarme z 8  es el central


    
