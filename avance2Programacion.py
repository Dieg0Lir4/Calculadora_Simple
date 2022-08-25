dinero = 500
comidaDePorkoj = 1000
numeroDePorkoj= 4
respuesta = ""

def InicioDelSimulador():
    print("¿Querires hacer?: Alimentar a los porkoj[a]      Vender a los porkoj[v]      Comprar[c]    Ver tus recursos[r]      Salir[e]")
    respuesta = input("Tu respuesta: ")
    if respuesta == "c":
        (IrAComprar())

    if respuesta == "a":
        IrAAlimentar()

    if respuesta == "v":
        IrAVender()
    
    if respuesta == "r":
        VerMisRecursos()
        
def VerMisRecursos():
    global dinero
    global numeroDePorkoj
    global comidaDePorkoj

    print("Tus recusos:")
    print("DINERO: " + str(dinero))
    print("NUMERO DE PORKOJ: " + str(numeroDePorkoj))
    print("COMIDA PARA LOS PORKOJ: " + str(comidaDePorkoj)+"kg")
    InicioDelSimulador()

def IrAComprar():
    global dinero
    global comidaDePorkoj
    global numeroDePorkoj
    print("Tu dinero es: $"+ str(dinero))
    print("Que quieres comprar:  200kg de comida de cerdo ($200) [c]   un porko ($S00) [p]")
    respuesta = input("Tu respuesta es: ")
    if respuesta == "c":
        dinero = dinero - 200
        comidaDePorkoj = comidaDePorkoj + 200

    if respuesta == "p":
        dinero = dinero - 500
        numeroDePorkoj = numeroDePorkoj + 1

    print("Tu dinero es: $"+ str(dinero))
    print("Tus porkoj son: " + str(numeroDePorkoj))
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
    print("Cuantos Porkoj vas a vender?")
    num1 = int(input("Tu respuesta es: ")) * 1000
    dineroBruto = int(num1)
    print("Te dieron $" + str(dineroBruto))
    print("Pero como eres una buena pareja le das la mitad a tu pareja")
    dinero = (dinero + num1/2)
    dinero = int(dinero)
    print("Tu dinero es: " + str(dinero)+"$")
    InicioDelSimulador()


InicioDelSimulador()




    
    
    
