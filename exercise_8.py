# Problem 8: "Simple range"

"""
Source: https://omegaup.com/arena/problem/Rango-simple/#problems
"""

# Pseudocode

# 1. Receive 3 inputs: a:int, b:list, c:list
# 2. Iterate over list b
# 3. Compare i elem of b with c[0] #Where c in the 0 position mean the beginning of the range
# 4. If b[i] >= c[0], continue to the next step
# 5. If b[i] <= c[1], continue to the next step
# 6. Count the element one by one....
# 7. Else: nothing happens
# 8. Return the counter
# 9. End


def simpleRange(a: int, b, c):  # Creating the Function with arguments
    counter = 0  # Create a var counter
    for i in range(0, len(b)):  # Iterate over the range
        if int(b[i]) >= int(c[0]):  # If b[i] >= c[0], continue to the next step
            if int(b[i]) <= int(c[1]):  # If b[i] <= c[1], continue to the next step
                counter += 1  # Count or sum 1 to the counter
        else:  # Else
            pass  # pass

    print(counter)  # print the var counter


a = int(input())  # Create a var of type int input
b = input().split()  # Create a var of type list (list of numbers given by a var)
c = input().split()  # Create a var of type list (list of numbers - range)

simpleRange(a, b, c)  # Call the function with the arguments
