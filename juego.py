import random



numeroSecreto = random.randint(1,101)
cantidadDeIntentos = 0
cantidadDeIntentosMax = 7
adivinado = False

print("Bienvenido al juego de adivinar el numero aleatorio")

while not adivinado:
    if not cantidadDeIntentos < cantidadDeIntentosMax:
        print("GAME OVER")
        break
    numero = int(input("Introduce un numero del 1 al 100:")) # el input recibe un string, el int lo cambia a int.
    
    if numero == numeroSecreto:
        print("Adivinaste!!!")
        adivinado = True
    elif numero < numeroSecreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    cantidadDeIntentos += 1

