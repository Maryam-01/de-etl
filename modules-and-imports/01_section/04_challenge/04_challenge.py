# Import the function from the utils.py file
# Import the numbers from the file in the nested data directory

# You should see the number 35
from data.nested_data.example_numbers import num_1 
from data.nested_data.example_numbers import num_2

from utils import sum_nums
result = sum_nums(num_1, num_2)
print(result)
