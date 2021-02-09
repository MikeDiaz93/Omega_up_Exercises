# Exercise 1 : "Dominant Vector"
"""
Source: 
https://omegaup.com/arena/problem/Vector-dominante

"""

# Solution 1


def solve(n: int, x, y):  # Define the function with their arguments
    cumple_condicion = 1  # Create a flag variable
    for i in range(0, n):  # Iterate over each element in the range of the number of elements of the vectors
        if x[i] < y[i]:  # If the first element of the first vector is less than the fisrt element of the second vector, the process will repeat for the same elements in the same position of each vector until the condition happens
            cumple_condicion = 0  # The flag variable is 0
            break  # If this condition happens, then break the iteration
        elif x[i] == y[i]:  # Elif, the first element of the first vector is equal to the fisrt element of the second vector
            cumple_condicion = 0  # The variable flag is 0
            break  # If this condition happens, then break the iteration
    # if the flag varible doesnt change its value, return the original value (1)
    return cumple_condicion

# Solution 2


def solve2(n, x, y):  # Define the function with their arguments
    for i in range(0, n):  # Iterate over each element in the range of the number of elements in vector
        if x[i] <= y[i]:  # if the first element of the first vector is less than the fisrt element of the second vector, the process will repeat for the same elements in the same position of each vector until the condition happens
            return 0                    # return 0
    return 1                            # if the condition doesnt happens, then return 1


n = input()  # Save the number of elements qwe want  for the vector
a = input().split()  # Save the 1st vector
b = input().split()  # Save the 2nd vector

res = solve(int(n), a, b)  # Save the function call in a variable
print(res)  # Print the result (call the function)
