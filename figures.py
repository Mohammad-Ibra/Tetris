import random

class Figure:

    """
    The figures and their rotations are drawn inside a 4x4 matrix
    Each figure will get assigned a type and color randomly.
    The image will be printed using the indices in the matrix that represents its blocks. 
    The rotate function will allow rotations of the figure.  
    """
    '''
    a = [
        [0 ,1 ,2 ,3 ],
        [4 ,5 ,6 ,7 ],
        [8 ,9 ,10,11],
        [12,13,14,15]
    ]
    '''

    __figures = {
        'square': [[5,6,9,10]], ## Square block and its rotations
        'J-block':[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], ## J block and its rotations
        'T-block':[[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], ## T block and its rotations
        'I-block':[[1, 5, 9, 13], [4, 5, 6, 7]], ## I block and its rotations
        'Z-block':[[4, 5, 9, 10], [2, 6, 5, 9]], ## z block and its rotations
        'S-block':[[6, 7, 9, 10], [1, 5, 6, 10]], ## s block and its rotations
        'L-block':[[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], ## L block and its rotations
    }

    __colors = {
        'RED': (255,0,0), ## RED
        'GREEN':(0,255,0), ## GREEN
        'BLUE':(0,0,255), ## BLUE
        'YELLOW':(255,255,0), ## YELLOW
        'PURPLE':(255,0,255) ## PURPLE
    } 

    def __init__(self, x = 10, y=0) -> None:
        self.x = x
        self.y = y
        self.type = random.choice([i for i in self.__figures.keys()])
        self.color = self.__colors[random.choice([i for i in self.__colors.keys()])]
        self.rotation = 0

    def image(self) -> list:
        return self.__figures[self.type][self.rotation]

    def rotate(self) -> None:
        self.rotation = (self.rotation + 1)% len(self.__figures[self.type])




    