
from XmlGenerator import XmlGenerator
from CalculateAlpha import CalculateAlpha
import math


class Controller (object):
    """
    Controller acts as the singleton class that hides
    implementation details of the alpha and pi.
    It generates the XML file and create DTD.
    In encapsulate the object of class CalculateAlpha
    """

    def get_length(self):
        """
        This method takes radius as an input from the user
        and computes the distance and return it as the output
        """
        try:
            # Taking radius as input from the user
            radius = float(input("Enter the radius of the circle :"))
            # Calculating the distance using the formula l = 2R(1 – cos(α/2))
            distance = 2 * radius * (1 - math.cos(alpha_calculator.get_alpha() / 2.0))
            print("The length of the segment X1-X2 is", distance, "units")
            xml = XmlGenerator()
            xml.generate_xml(radius, distance)
            xml.create_dtd()
            print("XML and DTD has been created")
            return distance

        # Handling Exception
        except Exception as e:
            print("Error, There is an exception", e)

alpha_calculator = CalculateAlpha()
controller = Controller()
controller.get_length()