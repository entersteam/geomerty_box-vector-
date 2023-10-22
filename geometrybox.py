import numpy as np

def unit_vector(vector):
    unit = vector / np.linalg.norm(vector)
    return unit

class ball():
    pos = [0,0]
    def __init__(self,pos,vector:np.ndarray,speed) -> None:
        self.pos = pos
        

if __name__ == '__main__':