import sys
import os
# MAKE YOUR CHANGES TO `sys.path` HERE

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "examples"))
)

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "01_section",
            "04_challenge",
            "data",
            "nested_data"
           
        )
    )
)



# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE

from file_5 import add
from example_numbers import num_1, num_2


print(add(num_1, num_2))
