#Enrique Jose Garcia A00827858
#Juan Carlos Triana Vela A00827629

from random import *
from turtle import *
from freegames import path

#Carga la imagen del carro
car = path('car.gif')
#Genera la lista de números
#Al ser parejas, solo se ocupan número del 0 al 32, 2 veces
tiles = list(range(32)) * 2
#Inicializa state
state = {'mark': None}
#Inicializa Hide que indica si las fichas han sido descubiertas
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    #Posición X y Y como punto de partida
    goto(x, y)
    down()
    #Set del color del contorno y del relleno
    color('black', 'white')
    begin_fill()
    #Al ser un cuadrado, ejecuta el ciclo 4 veces
    for count in range(4):
        #Avanza 50 px y gira 90°(360/4) 
        forward(50)
        left(90)
    end_fill()

#Función que genera un índice a partir de las coordenadas
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Función que retorna coordenadas a partir de un índice
#Las operaciones son inversas a las de index
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Función que lee los clicks
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    #Indice de la ficha clickeada
    spot = index(x, y)
    #Indice de la ficha anterior
    mark = state['mark']

    #Verifica si mark está vacío, si hemos hecho click en la misma
        #ficha o si el valor de la ficha anterior y la actual sonSs
        #diferentes
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        #Actualiza a mark con el índice nuevo
        state['mark'] = spot
    else:
        #Si las fichas son iguales entonces se descubren ambas fichas
        hide[spot] = False
        hide[mark] = False
        #Se hace None a marK
        state['mark'] = None

def draw():
    "Draw image and tiles."
    #Limpia la pantalla
    clear()
    #Se dirigie a 0,0
    goto(0, 0)
    #Carga la imagen del carro
    shape(car)
    #Copia la imagen de shape en la pantalla
    stamp()

    for count in range(64):
         #Si la ficha está oculta
        if hide[count]:
            #Dibuja un cuadrado, en la coordenada
            x, y = xy(count)
            square(x, y)

    #Carga la ficha seleccionada
    mark = state['mark']

    #Verifica si la ficha tiene algún valor y no ha sido
        #descubierta
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Va a una posición dentro de la casilla
        goto(x + 2, y)
        color('black')
        #Escribe el valor que tiene mark
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    
    
    #Actualiza el tablero
    update()
    
    juego_terminado = True
    
    for x in hide:
        if x==True:
            juego_terminado=False
            break
    if juego_terminado:
        print('El juego ha terminado')
        return
        
    
    
    
    
    ontimer(draw, 100)


#Revuelve la lista de tiles
shuffle(tiles)
#Set del tamaño y posición de la pantalla
setup(420, 420, 370, 0)
#Añade la figura del carro
addshape(car)
#Esconde el puntero
hideturtle()
#No muestra el reccorrido
tracer(False)
#Asigna la lectura del click a tap
onscreenclick(tap)
draw()
#Main Loop
done()