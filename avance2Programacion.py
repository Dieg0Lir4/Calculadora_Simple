from re import I
from time import sleep
from typing import Text



dinero = 500
comidaDePorkoj = 1000
numeroDePorkoj= 4
respuesta = ""

def InicioDelSimulador():

    Texto("Que quieres hacer")

    respuesta = input("Tu respuesta: ")
    if respuesta == "c":
        (IrAComprar())

    if respuesta == "a":
        IrAAlimentar()

    if respuesta == "v":
        IrAVender()
    
    if respuesta == "r":
        VerMisRecursos()
        
def Texto(textito):
    if(textito == "Que quieres hacer"):
        print()
        print("¿Querires hacer?")
        sleep(0.5)
        print("__________________________________")
        print("|  Alimentar a los porkoj    [a] |")
        print("|  Vender a los porkoj       [v] |")
        print("|  Comprar                   [c] |")
        print("|  Ver tus recursos          [r] |")
        print("|  Salir                     [e] |")
        print("----------------------------------")

    elif(textito == "Ver recursos"):
        print()
        print("Tus recusos:")
        sleep(0.5)
        print("_____________________________")
        print("| DINERO: " + str(dinero))
        print("| NUMERO DE PORKOJ: " + str(numeroDePorkoj))
        print("| COMIDA PARA LOS PORKOJ: " + str(comidaDePorkoj)+"kg")
        print("------------------------------")
        print()
        sleep(1)
        input("Dale al Enter para continuar")
        InicioDelSimulador()

def VerMisRecursos():
    global dinero
    global numeroDePorkoj
    global comidaDePorkoj

    Texto("Ver recursos")

def IrAComprar():
    global dinero
    global comidaDePorkoj
    global numeroDePorkoj
    print("Tu dinero es: $"+ str(dinero))
    print("Que quieres comprar:  200kg de comida de porko ($200) [c]   un porko ($500) [p]")
    respuesta = input("Tu respuesta es: ")
    if respuesta == "c":
        dinero = dinero - 200
        comidaDePorkoj = comidaDePorkoj + 200
        print("Tienes de comida para los porkoj: " + str(comidaDePorkoj) + "kg")

    if respuesta == "p":
        dinero = dinero - 500
        numeroDePorkoj = numeroDePorkoj + 1
        print("Tus porkoj son: " + str(numeroDePorkoj))

    print("Tu dinero es: $"+ str(dinero))
    
    
    InicioDelSimulador()

def IrAAlimentar():
    global comidaDePorkoj
    print("¿A cuantos porkoj vas a alimentar? (solo entero)")
    num1 = int(input("Tu respuesta es: "))
    print("¿Cuanta comida por porko? (solo entero)")
    num2 = int(input("Tu respuesta es: "))
    comidaDePorkoj = comidaDePorkoj - (num1 * num2)
    print("Tienes de comida para los porkoj: " + str(comidaDePorkoj) + "kg")
    InicioDelSimulador()

def IrAVender():
    global dinero
    global numeroDePorkoj
    print("Cuantos Porkoj vas a vender?")
    num1 = int(input("Tu respuesta es: "))
    numeroDePorkoj = numeroDePorkoj - num1
    dineroBruto = int(num1 * 1000)
    print("Te dieron $" + str(dineroBruto))
    print("Pero como eres una buena pareja le das la mitad a tu pareja")
    dinero = (dinero + num1/2)
    dinero = int(dinero)
    print("Tu dinero es: " + str(dinero)+"$")
    print("Te quedan: " + str(numeroDePorkoj) + " porkoj")
    InicioDelSimulador()

InicioDelSimulador()
