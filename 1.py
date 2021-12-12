"""
In this problem, your input is a list of integers, 
which represents the layout of a 3D structure, 
cubes arranged into towers in a row. 
The first number is the height of the first tower, 
the second is the height of the second and so on. 
The function has to calculate the surface area of the structure 
(we suppose the surface area of a single cube is 6 unit). 
If the input starts as [2, 1], then the first tower connects with 
the second one in 1 level, which means the surface area is 14 units.
"""
from typing import List  

def calculate_area(array:List[int]) -> int:
    return (4 * sum(array)) + 2 

print(calculate_area([2,1,8,7,1]))