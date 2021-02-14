# Problem 4: "Notes' average "
"""
Source: https://omegaup.com/arena/problem/Promedio-Calificaciones-/#problems
"""


"""
Averiguar como a partir de la entada por que/ como sale la salida 

1. Recibo la entrada 
2. Sumo todos los 7 elementos 
3. Divido entre el  total de elemtos: 7
4. Imprimo la division con un solo decimal  
 

for i in range -> arreglos , para tener mejor control de cada espacio
o 
while 

for in in len() -> arrglos, cuando no sabemos la longitud 

 
"""


def average(calificaciones):  # Create a Function with parameter
    # Apply the sum built-in function and save it in a var
    suma = sum(calificaciones)
    # Create a var to save result of the division
    promedio = suma / len(calificaciones)
    print("{:.1f}".format(promedio))  # Print the var result


calificaciones = input().split()  # Create a list var to save the n elements
