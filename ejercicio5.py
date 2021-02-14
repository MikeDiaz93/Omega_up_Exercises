# Problem 5: "Basic Counting"
"""
Source: https://omegaup.com/arena/problem/Conteos-basicos/#problems
"""


"""
Pseudocode

1. Recibo dos entradas (a, b)
2. Empiezo a contar a partir de la primera entrada hasta la segunda, uno por uno
3. Imprimo uno por uno por renglon

Nota: 
Cuando solomente quiero imprimir algunos datos pero no los necesito guardar
solo basta con que mande a llamar a mi funcion y dentro de mi funcion 
imprimir los resultados... 

"""


def printNumbers(a):  # Create a Function with a parameter a
    # Iterate over the range of the list of numbers: from n0 to nn
    for i in range(int(a[0]), int(a[1]) + 1):
        print(i)  # Print the i in the range of the numbers given


a = input().split()  # Create a list var with the range of the numbers we want to count
printNumbers(a)  # print Function
