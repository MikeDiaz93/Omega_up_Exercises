# Problem 3: "Multiplication of 2 vectors"
"""
Source : https://omegaup.com/arena/problem/Producto-punto-de-dos-vectores/
"""

"""
Entrada: 
n (int)
a (arr)
b (arr)

Pasos

1. mult arr[1] * arr2[1] 
2. guardando mult
3. avanzo y repito 1, 2 hasta n 
4 sumo elem del arr 
5. regreso sum total 

4
3,4,6,8
1,9,2,7
resultado_de_multipl = 3*1, 4*9, 6*2, 8*7 
return 107
 
"""


def multVect(n: int, a, b):  # Define the Function name with its parameters: n, a, b

    resultado = []  # Create a list var to save the multiplications result
    total = 0  # Create a var to save the sum of the multiplication
    for i in range(0, n):  # Iterate by each i in the range of 0-n
        # Append to the list var the mult of the i elem of the first vector by the i elem of the second vector
        resultado.append(int(a[i]) * int(b[i]))
    # Apply the sum built-in function to the list of the multiplications
    total = sum(resultado)

    return total    #


n = input()  # Create var 'n' with the number of inputs for the vector
a = input().split()  # Create list 'a' with vectors
b = input().split()  # Create another list 'b' with vectors

# Create a var calling the Function to multiply the vectors
prueba = multVect(int(n), a, b)
print(prueba)  # Print the var
