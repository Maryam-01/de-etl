# ADD YOUR IMPORTS HERE
import sys
import os
import math
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from examples.file_3 import number_list

# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE


def calculate_product(num_list):
    product = math.prod(num_list)
    return product


print(calculate_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
