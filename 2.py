"""
You will be given a square chess board with one queen and a number of obstacles
placed on it. Determine how many squares the queen can attack.

The function has the following parameters:

— int n: the number of rows and columns in the board
— int r_q: the row number of the queen's position
— int c_q: the column number of the queen's position
— int obstacles[k][2]: each element is an array of 2 integers, 
                        the row and column of an obstacle
Returns
— int: the number of squares the queen can attack
"""
from typing import List,Optional
import numpy as np

class Queen:
    def __init__(self,n:int,r_q:int,c_q:int,obstacles:Optional[List[List[int]]]= None) -> None:
        self.n = n
        self.r_q = r_q
        self.c_q = c_q
        self.obstacles = obstacles

        self.ups = []
        self.downs = []
        self.rights = []
        self.lefts = []
        self.uprights = []
        self.uplefts = []
        self.downrights = []
        self.downlefts = []

        self.possible_moves = []

    def check_if_obstacle(self,pos:List[int]) -> bool:
        if self.obstacles:
            if (pos in self.obstacles):
                return True
        if  (0 in pos) or (self.n+1 in pos):
                return True
        return False

    def get_up_values(self) -> None:
        for i in range(self.r_q+1,self.n+1):
            if self.check_if_obstacle([i,self.c_q]):
                return 
            self.ups.append([i,self.c_q])
    
    def get_down_values(self) -> None:
        for i in range(self.r_q-1,0,-1):
            if self.check_if_obstacle([i,self.c_q]):
                return 
            self.downs.append([i,self.c_q])
   
    def get_left_values(self) -> None:
        for i in range(self.c_q-1,0,-1):
            if self.check_if_obstacle([self.r_q,i]):
                return
            self.lefts.append([self.r_q,i])
         
    
    def get_right_values(self) -> None:
        for i in range(self.c_q+1,self.n+1):
            if self.check_if_obstacle([self.r_q,i]):
                return
            self.rights.append([self.r_q,i])
        
        
    def get_upright_values(self) -> None:
        for i,v in enumerate(range(self.c_q,self.n)):
            pos = [self.r_q+i+1,v+1]
            if self.check_if_obstacle(pos):
                return 
            self.uprights.append(pos)

    def get_upleft_values(self) -> None:
        for i,v in enumerate(range(self.c_q,1,-1)):
            pos = [self.r_q+i+1,v-1]
            if self.check_if_obstacle(pos):
                return 
            self.uplefts.append(pos)

    def get_downright_values(self) -> None:
        for i,v in enumerate(range(self.c_q,self.n)):
            pos = [self.r_q-i-1,v+1]
            if self.check_if_obstacle(pos):
                return 
            self.downrights.append(pos)

    def get_downleft_values(self) -> None:
        for i,v in enumerate(range(self.c_q,1,-1)):
            pos = [self.r_q-i-1,v-1]
            if self.check_if_obstacle(pos):
                return 
            self.downlefts.append(pos)

    def init_values(self) -> None:
        self.get_up_values()
        self.get_down_values()
        self.get_right_values()
        self.get_left_values()
        self.get_upright_values()
        self.get_upleft_values()
        self.get_downright_values()
        self.get_downleft_values()
        self.possible_moves = self.ups + self.downs + self.rights + self.lefts + self.uprights + self.uplefts +self.downlefts+self.downrights

    def convert_position(self,pos:List[int]) -> List[int]:
        pos[0] = abs(pos[0] - self.n)
        pos[1] = pos[1] - 1
        return pos

    def print_table(self) -> None:
        board = np.zeros((self.n,self.n),dtype=np.int64)
        #queen position
        qp = self.convert_position([self.r_q,self.c_q])
        board[qp[0],qp[1]] = 9
        #obstacles
        for o in self.obstacles:
           pos = self.convert_position(o) 
           board[pos[0],pos[1]] = 2
        #possible moves
        for p in self.possible_moves:
           pos = self.convert_position(p) 
           board[pos[0],pos[1]] = 1 
        print(board)

    @property
    def all_possible_moves(self) -> int:
        return len(self.possible_moves)

q = Queen(8,5,5,[[3,5],[7,7]])
q.init_values()
q.print_table()
print("Number of possible moves: ",q.all_possible_moves)



