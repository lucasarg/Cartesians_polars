'''
arreglar:
-pasarlo a ingles o español, ahora hay un spanglish
-los senos y cosenos tienen problemas cuando paso los 90° o 180°
-el formato 2D permite cambio de la ubicacion del observador, en el plano 3D el observador se mantiene en el punto  x,y,z = 0,0,0
-cuando las posiciones estan en 0, da error (porque no arregle eso de dividir por 0 aun)

mejoras previstas:
- Anticipacion/pronosticar ubicacion del objeto
- caluclar distancias relativas si el observador se encuentra en movimiento
'''
import os
import math

def menu():
    print('''
    --------- calc of artillery  -----------
    Opciones en 3D:
    1) De cartesianos a polares (3D)
    2) De polares a cartesianos (3D)


    Opciones en 2D:
    3) De cartesianos a polares (2D)
    4) De polares a cartesianos (2D)


    5) Info
    0) salir    
    ''')



def cartesianoPolares3D():
    os.system("cls")

    #    X  Y   Z
    #a = [10,10,10]
    a = [0,0,0]
    def input_coordinates():
        def print_map_empty():
                print(f'''
                         Z  
                         |     α XZ:   °
                         |      
                         |_ _ _ _ _ _ X
                        /
                       /   ß XY:    °
                   Y  /
        ''')

        print_map_empty()

        
        print("insert coordinates in: ")
        a[0] = int(input(' anxis "X": '))
        a[1] = int(input(' anxis "Y": '))
        a[2] = int(input(' anxis "Z": '))
        return a

    def distance(a):
        #diagonals of the plane
        diagonal_XYZ = round(math.sqrt(a[0]**2 + a[1]**2 + a[2]**2),2)
        diagonal_XY = round(math.sqrt(a[0]**2+a[1]**2),2)
        diagonal_XZ = round(math.sqrt(a[0]**2+a[2]**2),2) 
        diagonal_YZ = round(math.sqrt(a[1]**2+a[2]**2),2)

        print("\n")
        print("position of the objective ",a)
        print("\n")
        print("total distance(space XYZ) is: ",diagonal_XYZ, " units.")
        return diagonal_XYZ

    def angle(a):
        
        AngleXY = round((math.atan(a[1]/ a[0]) * 57.2958),2)
        AngleXZ = round(math.atan(a[2]/ a[0]) * 57.2958,2)

        def print_angle(AngleXY, AngleXZ):
            print(f'the angle XY is: {AngleXY}°')
            print(f'the angle XZ is: {AngleXZ}°')   
   
        def print_map(AngleXY, AngleXZ):

            print(f'''
                            Z  
                            |     α XZ: {AngleXZ}°
                            |                                /
                            |_ _ _ _ _ _ Z                  / lenght: 
                           /                               /
                          /   ß XY: {AngleXY}°
                     X   /
            ''')
        print_angle(AngleXY, AngleXZ)
        print_map(AngleXY, AngleXZ)
        
        
    input_coordinates()
    distance(a)
    angle(a)
    



def polaresCartesianos():

    def print_plane():
        print(f'''
                         Z  
                         |    
                         |      
                         |_ _ _ _ _ _ Y
                        /
                       /   
                   X  /
        ''')
    
    print_plane()
    distance = int(input("Isnsert distance: "))
    angleXZ =  math.polars(int(input("Insert angle XY in degrees: ")))
    angleXY =  math.polars(int(input("Insert angle XZ in degrees: ")))

 
    '''
    if angle.lower() == "rad":
        angle = int(input("inser angle in polars: "))
    else:
        angle = math.polars(int(angle))'''


    X = round(math.cos(angleXZ) * distance,2)
    Y = round(math.sin(angleXY) * distance,2)
    Z = round(math.sin(angleXZ) * distance,2)
    
    print(f'the objective finds in axisaxis X: {X}')
    print(f'the objective finds in axisaxis Y: {Y}')
    print(f'the objective finds in axisaxis Z: {Z}')
    

def cartesianoPolares2D():

    def print_matrix_empty():
        print('''
 
 Y  |
    |
    |
    |
 _ _|_ _ _ _ _ X
    |    
    |    ''')

  
    def inputs():
        print("insert next locations: ")
        obs = input("the observer will be placed in position (X,Y) = (0,0) ? (y/n)")   
        if obs.lower() == "y":
            my_horizontal = 0
            my_vertical = 0
            return my_vertical
        elif obs.lower() == "n":
            my_horizontal = int(input(" place of the observator in axis X: "))
            my_vertical = int(input(" place of the observator in axis Y: "))
        else:
            print("something went wrong")

        objective_X =  int(input(" place of the objective in axis X: "))
        objective_Y =  int(input(" place of the objective in axis Y: "))

        distance_Y = my_horizontal - objective_Y
        distance_X = my_vertical - objective_X
        
        def distanceAngle(distance_X,distance_Y):
            hypotenuse = round(math.sqrt((distance_Y) **2 + (distance_X) **2),4) 
            if distance_Y !=0:
                angle = (math.atan(distance_X/ distance_Y) * 57.2958)
            else:
                angle = 0
            print(f'The distance to objective is: {hypotenuse}')
            print(f'The angle is: {round(angle,2)}')
        distanceAngle(distance_X,distance_Y)



    print_matrix_empty()
    inputs()
    
def polarsCartesians2D():
    distance = int(input("insert distance: "))
    angle = input("insert angle in degrees(if you want in polars press 'rad' ): ")
    if angle.lower() == "rad":
        angle = int(input("inser angle in polars: "))
    else:
        angle = math.polars(int(angle))


    horizontal = round(math.cos(angle) * distance,2)
    vertical = round(math.sin(angle) * distance,2)
    
    print(f'the objective finds in axis X: {horizontal}')
    print(f'the objective finds in axis Y: {vertical}')



def instructions():
    print('''
    It is a program that transforms coordinates in 2D, from polars to cartesians and inverse
    
    The  option 1 "cartesians to polars" you insert the coordinates in the X, Y and Z anxis,
    from the viewer and the objective, and returns the total distance, and angle
    In the version of artillery, it is useful when you have the coordinates in a map and need to calculate the angle and distance to achieve the objective.

    The option 2 "polars to cartesians" you insert the data in polars (distance, and angles) and return it in cartesians
    Imagine a radar where it gives you the distance and angles,then you can use this data to put the objective in a map (in 3D you can see the height)

    Next versions:
    the proyect is to cont and add pronostics, that is to calculate the position across the time and where it will be

    this program was built by Tamburo Lucas
    email: tamburolucas@gmail.com
    github: https://github.com/lucasarg
    ''')

def start(): 
    cont = True
    while cont == True:
        os.system("cls")        
        menu()
        option1 = int(input("Insert an option: "))
        if option1 == 1:
            cartesianoPolares3D()
        elif option1 == 2:
            polaresCartesianos()
        elif option1 == 3:
            cartesianoPolares2D()
        elif option1 == 4:
            polarsCartesians2D()
        elif option1 == 5:
            instructions()
        elif option1 == 0:
            cont = False
            print("closing...")
        else:
            print("no se te entendio un pingo ")
        input(print("press 'enter' to cont"))
    input("Good bye")

if __name__ == '__main__':
    start()


