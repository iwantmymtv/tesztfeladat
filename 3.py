"""
Create a function which produces an 𝑛×𝑛 array which contains ±1 numbers 
like a chessboard. (𝑀𝑖,𝑗=(−1)i+j). 
"""
import numpy as np
import numpy.typing as npt

def generate_matrix(n:int) -> npt.NDArray[np.int64]:
    arr = np.empty((n,n),dtype=np.int64)
    for i in range(n):
        for j in range(n):
            arr[i][j] = (-1) ** (i+j)
    return arr

 
print(generate_matrix(4))