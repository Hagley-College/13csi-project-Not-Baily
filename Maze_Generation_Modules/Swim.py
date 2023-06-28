import colorama

"""
Title: Ocean
Author: Bailey Reid
Date: 29/07/22
Version: 1.0
Purpose: To Create The Player Used To Play The Maze
"""




class Sprite:
    '''Creates the avatars to be placed on the maze'''
    def __init__(self,name,row,col):
        self.name = name
        self.row = row
        self.col = col
    def print(self):
        print(f"{self.name}'s row is {self.row} and col is {self.col}\n")
    def move(self,direction,distance,ocean):
        '''Allows Boris and the Bag (Goal) to be moved so you can actually finish the maze'''
        if direction =='down' and self.row < ocean.HEIGHT-1:
            if "e" in ocean.get(self.row+distance,self.col):
                self.row = self.row+distance

        elif direction=="up" and self.row > 0:
            if "e" in ocean.get(self.row-distance,self.col):
                self.row = self.row-distance

        elif direction == "left" and self.col > 0:
            if "e" in ocean.get(self.row,self.col-distance):
                self.col = self.col-distance

        elif direction == "right" and self.col < ocean.WIDTH-1:
            if "e" in ocean.get(self.row,self.col+distance):
                self.col = self.col+distance
    def restartS(self,row,col):
        '''Moves both Bois and the Bag (Goal) back to their starting positions'''
        self.row = row
        self.col = col
    
    def hit(self,a,b):
        '''Creates the system that allows collisions to be detected'''
        if a.row == b.row and a.col == b.col:
            return True
        else:
            return False