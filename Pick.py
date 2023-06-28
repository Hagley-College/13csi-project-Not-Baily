import colorama
import termcolor
"""
Title: Ocean
Author: Bailey Reid
Date: 29/07/22
Version: 1.0
Purpose: To Create The Player Used To Play The Maze
"""



class Pick:
    
    def __init__(self,name,row,col):
        self.name = name
        self.row = row
        self.col = col

    def move(self,direction,distance,ocean):
        
        if direction =='down' and self.row < ocean.HEIGHT-1:
            if 'e' in ocean.get(self.row+distance,self.col):
                self.row = self.row+distance

        elif direction=="up" and self.row > 0:
            if 'e' in ocean.get(self.row-distance,self.col):
                self.row = self.row-distance

        elif direction == "left" and self.col > 0:
            if 'e' in ocean.get(self.row,self.col-distance):
                self.col = self.col-distance

        elif direction == "right" and self.col < ocean.WIDTH-1:
            if 'e' in ocean.get(self.row,self.col+distance):
                self.col = self.col+distance
    def restartS(self,row,col):
        self.row = row
        self.col = col
