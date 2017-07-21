import math
# This function gives the length of the segment X1X2 as described in the specification of Cheers!
# Formula for calculating length of the segment is l = 2R(1 – cos(α/2)),
from CalculateAlpha import CalculateAlpha


def get_length():
    radius = float(input("Enter the radius of the circle :"))
    alpha_calculator = CalculateAlpha();
    distance = 2 * radius * (1 - math.cos(alpha_calculator.get_alpha() / 2.0))
    print("The length of the segment X1-X2 is", distance, "units")


get_length()












