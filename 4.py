"""
Create a function which computes the Euclidean norm of each line for a 2D array. 
Use numpy operations and vectorization, avoid for cycles. 
"""
from typing import Union,List
import numpy as np
import numpy.typing as npt

def normailze(array:Union[List[Union[int,float]],npt.NDArray]) -> np.array:
    return np.sqrt(np.sum(np.square(array),axis=1))

X = np.arange(10)[:, None]*np.ones((10, 5));
print(normailze(X))
