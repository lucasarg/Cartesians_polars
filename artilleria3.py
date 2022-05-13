'''
arreglar:
-

mejoras:
- pasarlo a 3D
- Anticipacion/pronosticar
- 


'''
import os
import math

def menu():
    print('''
    --------- calculo de artilleria  -----------
    1) De cartesianos a radianes
    2) De radianes a cartesianos (en contstruccion)

    
    0) salir    
    ''')



def cartesianoRadianes():

    matriz = []
    def matrix():
        nonlocal matriz
        size = 10
        #size = int(input("insert size of the map"))
        for i in range(size):
            matriz.append([])
            for j in range(size):
                matriz[i].append("_")
    matrix()


        #aqui esta el ingreso, pero lo apagamos mientras lo estamos construyendo

    mi_horizontal =  int(input("ingrese su ubicacion horizontal en el mapa: "))
    mi_vertical =  int(input("ingrese su ubicacion vertical en el mapa: "))
    objetivo_horizontal =  int(input("ingrese la ubicacion horizontal del objetivo en el mapa: "))
    objetivo_vertical =  int(input("ingrese la ubicacion vertical del objetivo en el mapa: "))
    '''
    mi_vertical = 2
    mi_horizontal = 2
    objetivo_vertical = 5
    objetivo_horizontal = 7
    '''
    matriz[objetivo_horizontal][objetivo_vertical] = "X"
    matriz[mi_horizontal][mi_vertical] = "Y"

    distancia_alto = mi_vertical - objetivo_vertical
    distancia_ancho = mi_horizontal - objetivo_horizontal
    '''
    def referencias():
        print(f'el objetivo se encuentra verticalmente a {mi_vertical-objetivo_vertical} ')
        print(f'el objetivo se encuentra horizontalmente a {mi_horizontal-objetivo_horizontal} ')

    referencias()'''
    
    def distanciaAngulo():
        hipotenusa = round(math.sqrt((mi_vertical-objetivo_vertical) **2 + (mi_horizontal-objetivo_horizontal) **2),4) 
        angulo = math.atan(distancia_ancho/ distancia_alto) * 57.2958
        print(f'la distancia al objetivo es: {hipotenusa}')
        print(f' el angulo es: {angulo}')

    distanciaAngulo()
    def print_matriz(matriz):

        for i in matriz:
            print(i)
    print_matriz(matriz)




def radianesCartesianos():
    distance = int(input("insert distance: "))
    angle = input("insert angle in degrees(if you want in radians press 'rad' ): ")
    if angle.lower() == "rad":
        angle = int(input("inser angle in radians: "))
    else:
        angle = math.radians(int(angle))


    horizontal = round(math.cos(angle) * distance,2)
    vertical = round(math.sin(angle) * distance,2)
    
    print(f'el objetivo se encuentra horizontalmente {horizontal}')
    print(f'el objetivo se encuentra verticalmente {vertical}')

def inicio():
    continuar = True
    while continuar == True:
        os.system("cls")        
        menu()
        opcionInicial = int(input("Inserte una opcion: "))
        if opcionInicial == 1:
            cartesianoRadianes()
        elif opcionInicial == 2:
            radianesCartesianos()
        elif opcionInicial == 3:
            pass
        elif opcionInicial == 4:
            pass
        elif opcionInicial == 0:
            continuar = False
            print("closing...")
        else:
            print("no se te entendio un pingo culiao")
        input(print("press 'enter' to continue"))
    input("hasta luego")

if __name__ == '__main__':
    inicio()