'''
arreglar:
-pasarlo a ingles o español, ahora hay un spanglish
-los senos y cosenos tienen problemas cuando paso los 90°
-el formato 2D permite cambio de la ubicacion del observador, en el plano 3D el observador se mantiene en el punto  x,y,z = 0,0,0

mejoras:
- pasarlo a 3D (done)
- Anticipacion/pronosticar
- 
'''
import os
import math

def menu():
    print('''
    --------- calc of artillery  -----------
    1) De cartesianos a radianes (3D)
    2) De radianes a cartesianos (3D)

    Opciones en 2D:
    3) De cartesianos a radianes (2D)
    4) De radianes a cartesianos (2D)

    5) Info
    0) salir    
    ''')



def cartesianoRadianes():
    os.system("cls")

    #    X  Y   Z
    #a = [10,10,10]
    a = [0,0,0]
    def input_coordinates():
        print("insert coordinates in: ")
        a[0] = int(input(' anxis "X": '))
        a[1] = int(input(' anxis "Y": '))
        a[2] = int(input(' anxis "Z": '))
        return a

    def distance(a):
        diagonal_XYZ = round(math.sqrt(a[0]**2 + a[1]**2 + a[2]**2),2)
        diagonal_XY = round(math.sqrt(a[0]**2+a[1]**2),2)
        diagonal_XZ = round(math.sqrt(a[0]**2+a[2]**2),2) 
        diagonal_YZ = round(math.sqrt(a[1]**2+a[2]**2),2)

        print("position of the objective ",a)
        print("the distance in the plane XY",diagonal_XY)
        print("the distance in the plane XZ",diagonal_XZ)
        print("the distance in the plane YZ",diagonal_YZ)
        print("total distance(space XYZ) is: ",diagonal_XYZ)

    def angle(a):
        
        AngleXY = round((math.atan(a[1]/ a[0]) * 57.2958),2)

        AngleXZ = round(math.atan(a[1]/ math.sqrt(a[0]**2+a[1]**2)) * 57.2958,2)
        print(f'the angle XY is: {AngleXY}')
        print(f'the angle XZ is: {AngleXZ}')   
        return AngleXY, AngleXZ


    
    input_coordinates()
    angle(a)
    distance(a)

def radianesCartesianos():
    distance = int(input("insert distance: "))
    angleXZ =  math.radians(int(input("insert angle XY in degrees: ")))
    angleXY =  math.radians(int(input("insert angle XZ in degrees: ")))
 
    '''
    if angle.lower() == "rad":
        angle = int(input("inser angle in radians: "))
    else:
        angle = math.radians(int(angle))'''


    X = round(math.cos(angleXZ) * distance,2)
    Y = round(math.sin(angleXY) * distance,2)
    Z = round(math.sin(angleXZ) * distance,2)
    
    print(f'el objetivo se encuentra eje X {X}')
    print(f'el objetivo se encuentra eje Y {Y}')
    print(f'el objetivo se encuentra eje Z {Z}')
    

def cartesianoRadianes2D():

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

    print("ingrese las siguentes ubicaciones: ")
    mi_horizontal =  int(input("su ubicacion horizontal (eje x): "))
    mi_vertical =  int(input("su ubicacion vertical (eje y): "))
    objetivo_horizontal =  int(input(" ubicacion horizontal del objetivo (eje x): "))
    objetivo_vertical =  int(input(" ubicacion vertical del objetivo (eje y): "))

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
        if distancia_alto !=0:
            angulo = (math.atan(distancia_ancho/ distancia_alto) * 57.2958)
        else:
            angulo = 0
        print(f'La distancia al objetivo es: {hipotenusa}')
        print(f'El angulo es: {round(angulo,2)}')

    distanciaAngulo()
    def print_matriz(matriz):

        for i in matriz:
            print(i)
    print_matriz(matriz)




def radianesCartesianos2D():
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



def instrucciones():
    print('''
    It is a program that transforms coordinates in 2D, from radiands to cartesians and inverse
    
    The  option 1 "cartesians to radians" you insert the coordinates in the X anxi and later Y anxi,
    from the viewer and the objective, and returns the total distance, and angle
    In the version of artillery, it is useful when you have the coordinates in a map and need to calculate the angle and distance to achieve the objective.

    The option 2 "radians to cartesians" you insert the data in radians and return in cartesians
    In a artillery situation, you can have a view of an objective and use this data to put the information in a map



    Next versions:
    the proyect is to continue this in a 3D model, and add pronostics, that is to calculate the position across the time and where it will be

    this program was built by Tamburo Lucas
    email: tamburolucas@gmail.com
    github: https://github.com/lucasarg
    ''')

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
            cartesianoRadianes2D()
        elif opcionInicial == 4:
            radianesCartesianos2D()
        elif opcionInicial == 5:
            instrucciones()
        elif opcionInicial == 0:
            continuar = False
            print("closing...")
        else:
            print("no se te entendio un pingo culiao")
        input(print("press 'enter' to continue"))
    input("hasta luego")

if __name__ == '__main__':
    inicio()


