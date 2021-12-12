"""
Create a function which expects any number of square matrices and
 outputs a block-matrix which contains the input matrices in its main diagonal,
  and contains 0 in every other place.
"""
from typing import List,Union
import numpy as np
import numpy.typing as npt

def create_block_matrix(matrices:npt.NDArray[npt.NDArray]) -> npt.NDArray:
    #get the height of the array
    m = len(matrices[0])
    n = m*len(matrices)
    #create the array
    a = np.zeros((n,n))

    for i in range(len(matrices)):
        a[i*m:i*m+m,i*m:i*m+m] = matrices[i]

    return a

input_array = np.array([np.arange(16).reshape(4,4) for i in range(2)])
input_array2 = np.array([np.arange(4).reshape(2,2) for i in range(5)])

#print(create_block_matrix(input_array))
print(create_block_matrix(input_array2))