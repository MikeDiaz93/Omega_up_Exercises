# Problem 7: "All the numbers divided between 2 numbers"

"""
Source: https://www.programiz.com/python-programming/online-compiler/
"""

# Pseudocode

# 1. Receive 2 arguments in the functions : a, b
# 2. Verify that a or b are not negative numbers
# 3. If the previous step happens, print "Error"
# 4. Verify that a >= b
# 5. If the previous step happens, print "Error"
# 6. Verify if a is odd or even
# 7. If a is even
# 8. Print even number from a to b range.
# 9. Else (They are odd numbers)
# 10. Print odd numbers from a to b range
# 11. End


def allNumbers(a: int, b: int):  # Create function with int arguments : a and b
    if a < 0 or b < 0:  # If a <0 or b<0
        print("Error")  # Print "Error"
    elif a >= b:  # elif a>=b
        print("Error")  # Print "Error"
    else:  # Else
        if a % 2 == 0:  # If a%2 equals  0
            for i in range(a, b):  # Iterate over the range a-b
                if i % 2 != 0:  # If i%2 different of 0
                    print(i, end=" ")  # Print elem with spaces between them
        else:  # Else
            for i in range(a, b):  # Iterate over the range a-b
                if i % 2 == 0:  # If i%2 equals 0
                    print(i, end=" ")  # Print elem with spaces between them

    return 0  # Return 0


a = int(input())  # Create var of type int
b = int(input())  # Create var of type int

allNumbers(a, b)  # Call function with arguments
