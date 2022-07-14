from tkinter import Grid
from figures import Figure
import pygame
import numpy as np

class Tetris:

    def __init__(self, width, height) -> None:
        self.figure = Figure(6, 0)
        self.width = width
        self.height = height
        self.rows = height//20
        self.cols = width//20
        self.grid = np.zeros((self.rows, self.cols))
        self.frozen = False
        self.score = 0
        self.state = "start"

    def draw_figure(self, surface):
        shape = self.figure.image()
        for i in range(4):
            for j in range(4):
                p = 4*i + j
                if p in shape:
                    pygame.draw.rect(surface, self.figure.color, (20*(self.figure.x+j) + 1, 20*(self.figure.y + i) + 1,18,18))

        pygame.display.update()

    
    def go_down(self):
        if self.frozen == False:
            self.figure.y += 1
        if self.check_collision():
            self.freeze()
            self.new_piece()
            self.figure.y -= 1

    def go_left(self):
        if self.frozen == False:
            self.figure.x -= 1
        if self.check_collision():
            self.figure.x +=1

    def go_right(self):
        if self.frozen == False:
            self.figure.x += 1
        if self.check_collision():
            self.figure.x -=1

    def check_collision(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if 20*(i + self.figure.y) > (self.height - 1) or 20*(j + self.figure.x) > (self.width - 1) or (j + self.figure.x )< 0 or self.grid[i + self.figure.y][j + self.figure.x] > 0:
                        return True
        return intersection

    def freeze(self):
        if self.check_collision():
            self.frozen = True
            for i in range(4):
                for j in range(4):
                    if j * 4 + i in self.figure.image():
                        self.grid[self.figure.y+j-1][self.figure.x+i] = 1
            self.break_line()

    def new_piece(self):
        self.figure = Figure(6,0)
        self.frozen = False
        if self.check_collision():
            self.state = "game over!"

    def break_line(self):

        for row in range(len(self.grid)):
            sum = 0
            for i in range(len(self.grid[row])):
                if self.grid[row][i]>0:
                    sum += 1
            if sum == len(self.grid[row]):
                new = self.__translate_grid(self.grid[:(row+1)])
                new = np.append(new, self.grid[(row+1):], axis=0)
                self.grid = new
                self.score += 1

    def __translate_grid(self, grid):
        prev = np.zeros(self.cols)
        new = []
        for i in grid:
            curr = i
            i = prev
            prev = curr
            new.append(i)
        new = np.array(new)
        return new



                

        
