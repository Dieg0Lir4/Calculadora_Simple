from datetime import date, datetime
from distutils.command.clean import clean
import os
import random
from re import I
from time import sleep
from traceback import print_tb
from typing import Text





dinero = 500
comidaDePorkoj = 1000
numeroDePorkoj= 0
respuesta = ""
nombreDeTusPorkoj = []
pesoDeTusPorkoj = []
añosDeTusPorkoj = []
indiceDeTusPorkoj = []
diaDeInicio = date.today()


def InicioDelSimulador():
    os.system("clear")
    Texto("¿Que quieres hacer?")

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
    if(textito == "¿Que quieres hacer?"):
        os.system("clear")
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
        os.system("clear")
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
        respuesta = input("¿Quieres visitar a tus porkoj? (s/n)")
        if respuesta == "s":
            Texto("visitar a los cerdos")
            input("DALE ENTER PARA CONTINUAR")
            InicioDelSimulador()
        else:    
            InicioDelSimulador()
        
    elif(textito == "¿Que quieres comprar?"):
        print("_________________________________________")
        print("|  200kg de comida de porko ($200) [c]  |") 
        print("|  1 nuevo porko ($500)            [p]  |")
        print("-----------------------------------------")

    elif(textito == "visitar a los cerdos"):
        for i in range(len(nombreDeTusPorkoj)):

            print(f"\n\nNOMBRE: {nombreDeTusPorkoj[i]}")
            print(f"PESO: {pesoDeTusPorkoj[i]}")
            print(f"AÑOS: {añosDeTusPorkoj[i]}")
            print(f"INDICE: {indiceDeTusPorkoj[i]}")

def Textote(texto):
    os.system("clear")
    if texto == "FARMER SIMULATOR":
        respuesta = ""
        print("\nd88888b  .d8b.  d8888b. .88b  d88. d88888b d8888b.      .d8888. d888888b .88b  d88. db    db db       .d8b.  d888888b  .d88b.  d8888b. \n88'     d8' `8b 88  `8D 88'YbdP`88 88'     88  `8D      88'  YP   `88'   88'YbdP`88 88    88 88      d8' `8b `~~88~~' .8P  Y8. 88  `8D \n88ooo   88ooo88 88oobY' 88  88  88 88ooooo 88oobY'      `8bo.      88    88  88  88 88    88 88      88ooo88    88    88    88 88oobY' \n88~~~   88~~~88 88`8b   88  88  88 88~~~~~ 88`8b          `Y8b.    88    88  88  88 88    88 88      88~~~88    88    88    88 88`8b   \n88      88   88 88 `88. 88  88  88 88.     88 `88.      db   8D   .88.   88  88  88 88b  d88 88booo. 88   88    88    `8b  d8' 88 `88. \nYP      YP   YP 88   YD YP  YP  YP Y88888P 88   YD      `8888Y' Y888888P YP  YP  YP ~Y8888P' Y88888P YP   YP    YP     `Y88P'  88   YD ")
        input("\n\n\nDALE AL ENTER")

def VerMisRecursos():
    
    Texto("Ver recursos")

def IrAComprar():
    global dinero
    global comidaDePorkoj
    global numeroDePorkoj

    quererComprar = True
    while quererComprar:
        os.system("clear")
        sleep(0.2)
        print("RECURSOS")
        print("_____________________________")
        print("| Tienes de dinero: $" + str(dinero))
        print("| Tienes: " + str(numeroDePorkoj) + " porkoj")
        print("| Tienes de comida para los porkoj: " + str(comidaDePorkoj)+"kg")
        print("------------------------------")
        sleep(0.2)
        print("\n¿Que quieres comprar?")
        Texto("¿Que quieres comprar?")
        
        respuesta = input("Tu respuesta es: ")
        if respuesta == "c":
            dinero = dinero - 200
            comidaDePorkoj = comidaDePorkoj + 200
            print("Tienes de comida para los porkoj: " + str(comidaDePorkoj) + "kg")

        if respuesta == "p":
            dinero = dinero - 500
            numeroDePorkoj = numeroDePorkoj + 1
            print("\nPonle un nombre a tu porko")
            nombreDelPorkoj = str(input("Su nombre: "))
            nombreDeTusPorkoj.append(nombreDelPorkoj)
            pesoDeTusPorkoj.append(round(random.uniform(5.0, 10.0),2))
            añosDeTusPorkoj.append(round(random.uniform(0.1, 3.0),1))
            indiceDeTusPorkoj.append(numeroDePorkoj)
            sleep(0.2)
            os.system("clear")
            print("FELICIDADES!!!")
            print(f"Compraste a {nombreDelPorkoj},\nCon un peso inicial de: {pesoDeTusPorkoj[numeroDePorkoj-1]}kg\nTiene {añosDeTusPorkoj[numeroDePorkoj-1]} años \nSu indice es: {len(indiceDeTusPorkoj)}")
            sleep(0.4)
            print("Ahora tienes: " + str(numeroDePorkoj) + " porkoj")

        print("\nTu dinero es: $"+ str(dinero))
        sleep(0.5)
        respuesta = input("\n¿Quieres voler a comprar? (s/n)")
        if respuesta != "s":
            quererComprar = False
            

        
    
    
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
    int("\nDALE ENTER PARA CONTINUAR")
    InicioDelSimulador()



Textote("FARMER SIMULATOR")
InicioDelSimulador()
