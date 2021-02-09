# Problem 2: "Filtering multiples"
"""
Source: https://omegaup.com/arena/problem/Filtrando-multiplos/
"""


def putX(n: int,  k: int, arr):  # Define the function with their parameters (n= number of elements, k = multiple number) as inegers and  arr = array of numbers )
    i = 0  # crete a count initilizer
    while i < n:  # while i is less than 0
        # If the remainder of the n element as int and the k number is different from 0
        if int(arr[i]) % k != 0:
            # Replace and print X instead of the n number of the array with an space between the print elements
            print("X", end=" ")
        else:  # Else
            # Print as string the n elements with an space between them
            print(str(arr[i]), end=" ")
        i += 1  # Iterate over the array


n = input()  # Input the number of elements of the array
arr = input().split()  # Input and split of the array
k = input()  # Input the number we want to look for their multiples

putX(int(n), int(k), arr)  # call the function
