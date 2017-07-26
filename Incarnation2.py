
from XmlGenerator import XmlGenerator
import math


# Formula for calculating length of the segment is l = 2R(1 – cos(α/2)),
from CalculateAlpha import CalculateAlpha

radius = float(input("Enter the radius of the circle :"))
# creating instance of class CalculateAlpha
alpha_calculator = CalculateAlpha()
distance = 2 * radius * (1 - math.cos(alpha_calculator.get_alpha() / 2.0))
print("The length of the segment X1-X2 is", distance, "units")













