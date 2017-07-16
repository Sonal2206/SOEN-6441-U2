import math
# This function computes the value of alpha using the equation α – sin(α) = π/2.
def alpha():
    old_alpha = None
    # approximate value of the alpha
    new_alpha = 2.0

    while new_alpha != old_alpha:
        old_alpha = new_alpha
        new_alpha = math.sin(old_alpha) + (get_pi(1000)/2.0)
        new_alpha = round(new_alpha,4)
    return new_alpha
    print("The value of alpha is",alpha())
# This function gives the length of the segment X1X2 as described in the specification of Cheers!
# Formula for calculating length of the segment is l = 2R(1 – cos(α/2)),
def length():
     radius = int(input("Enter the radius of the circle :"))
     length = 2* radius *(1-math.cos(alpha()/2.0))
     print("The length of the segment X1-X2 is",length, "units")
# This function calculates the approximate value of PI using Leibniz algorithm

def get_pi(terms):
    result = 0.0
    for n in range(terms):
        result += (-1.0) ** n / (2.0 * n + 1.0)
    return 4 * result


get_pi(1000)
alpha()
length()












