import random
import imp
import copy
from tkinter import filedialog as fd, messagebox as mb

"""
Title: Ocean
Author: Bailey Reid
Date: 29/07/22
Version: 1.0
Purpose: To Create The Infomation That The Main File Uses To Create The Visable Maze
"""

defultM = [['wb', 'wt', 'wp', 'wt', 'wt', 'wt', 'wl', 'ed', 'wb', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'ws'],
['wg', 'ed', 'wu', 'eb', 'et', 'et', 'et', 'ej', 'wg', 'eb', 'et', 'et', 'et', 'ep', 'et', 'et', 'et', 'et', 'es', 'wg'],
['wg', 'ec', 'et', 'ei', 'wb', 'wt', 'wt', 'wt', 'wj', 'eg', 'wb', 'wt', 'ws', 'eg', 'wb', 'wt', 'wp', 'ws', 'eg', 'wg'],
['wx', 'wt', 'ws', 'eg', 'wu', 'eb', 'et', 'et', 'et', 'ej', 'wg', 'ed', 'wg', 'eg', 'wg', 'ed', 'wc', 'wj', 'eg', 'wg'],
['wg', 'ed', 'wg', 'ec', 'et', 'ej', 'wb', 'wt', 'wt', 'wt', 'wj', 'eg', 'wg', 'eg', 'wu', 'ec', 'ep', 'et', 'ei', 'wg'],
['wg', 'eg', 'wx', 'wt', 'wt', 'wp', 'wi', 'eb', 'et', 'et', 'et', 'ei', 'wg', 'ex', 'el', 'wn', 'eg', 'wd', 'eg', 'wg'],
['wg', 'eg', 'wu', 'eb', 'el', 'wc', 'wi', 'eg', 'wb', 'wt', 'wl', 'eg', 'wg', 'eg', 'wd', 'eb', 'ej', 'wu', 'eg', 'wg'],
['wg', 'ex', 'et', 'ei', 'wn', 'ed', 'wg', 'eg', 'wg', 'eb', 'et', 'ej', 'wg', 'eg', 'wg', 'eg', 'wd', 'eb', 'ej', 'wg'],
['wg', 'eg', 'wd', 'ec', 'et', 'ei', 'wu', 'eg', 'wg', 'eg', 'wr', 'wt', 'wj', 'eg', 'wg', 'eg', 'wg', 'eg', 'wr', 'wi'],
['wg', 'eg', 'wc', 'wt', 'wl', 'ec', 'et', 'ej', 'wg', 'ec', 'et', 'et', 'et', 'ej', 'wu', 'eg', 'wg', 'ex', 'es', 'wg'],
['wg', 'ec', 'ep', 'et', 'es', 'wb', 'wt', 'wt', 'wq', 'wt', 'wt', 'wt', 'wt', 'ws', 'eb', 'ej', 'wu', 'ex', 'ei', 'wg'],
['wx', 'wl', 'eg', 'wd', 'eg', 'wg', 'er', 'ep', 'et', 'ep', 'et', 'et', 'es', 'wg', 'eg', 'wd', 'eb', 'eq', 'ej', 'wg'],
['wg', 'eb', 'ei', 'wg', 'eg', 'wc', 'wl', 'eg', 'wd', 'eu', 'wr', 'wl', 'eg', 'wu', 'eg', 'wg', 'eg', 'wb', 'wt', 'wi'],
['wg', 'ec', 'ei', 'wg', 'ec', 'et', 'et', 'ej', 'wx', 'wl', 'er', 'et', 'ea', 'et', 'ej', 'wg', 'eg', 'wg', 'ed', 'wg'],
['wx', 'wl', 'eg', 'wc', 'wp', 'wp', 'wt', 'wp', 'wj', 'ed', 'wr', 'wl', 'eu', 'wr', 'wt', 'wj', 'eg', 'wg', 'eg', 'wg'],
['wg', 'er', 'eq', 'es', 'wc', 'wj', 'ed', 'wg', 'eb', 'eq', 'et', 'es', 'wn', 'eb', 'et', 'et', 'ej', 'wu', 'eg', 'wg'],
['wx', 'wt', 'ws', 'ex', 'et', 'et', 'ei', 'wg', 'eg', 'wr', 'ws', 'ec', 'et', 'ej', 'wr', 'wt', 'wl', 'eb', 'ei', 'wg'],
['wg', 'ed', 'wu', 'eg', 'wb', 'wl', 'eg', 'wg', 'ec', 'es', 'wc', 'wt', 'wt', 'wl', 'eb', 'et', 'ep', 'eq', 'ei', 'wg'],
['wg', 'ec', 'et', 'ej', 'wg', 'er', 'ej', 'wx', 'ws', 'ec', 'et', 'et', 'et', 'et', 'ej', 'wd', 'eu', 'wd', 'eg', 'wg'],
['wc', 'wt', 'wt', 'wt', 'wq', 'wt', 'wt', 'wq', 'wq', 'wt', 'wt', 'wt', 'wt', 'wt', 'wt', 'wq', 'wt', 'wj', 'eu', 'wu']]

filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

streamline = True
class Ocean():
    
    

    def loadm(file = ".\Mazes\Maze10x1.txt"):
        tmap = []
        
        file = fd.askopenfile(filetypes=filetypes)
        print(file)
        tmap:list[str] = file.readlines()
        lmap:list[list[str]] = []
        line_size = tmap.pop(0).removesuffix('\n').split(' ')
        line_start = tmap.pop(0).removesuffix('\n').split(' ')

        for n in range(len(tmap)):

            tmap[n] = tmap[n].strip('\n')

            line = []
            for mmmmm in tmap[n]: 
                line.append(mmmmm)

            lmap.append(line)


        tmap = copy.deepcopy(lmap)

        
        PX, PY, GX, GY = int(line_start[0]), int(line_start[1]), int(line_start[2]), int(line_start[3]) 
        WIDTH, HEIGHT = int(line_size[0]), int(line_size[1]) 
        return tmap,PX,PY,GX,GY,WIDTH,HEIGHT
    
    if streamline == False:
        deorfi = mb.askquestion(message="Do You Want to Open From File?")
    else:
        deorfi = "no"

    if deorfi == "yes":
        tmap,PX,PY,GX,GY,WIDTH,HEIGHT = loadm()
    else:
        WIDTH = 20
        HEIGHT = 20
        tmap = defultM
        PX = 7
        PY = 0
        GX = 18
        GY = 19

    
    def print(shelf):
        for row in shelf.tmap:
            print(row )
    def get(shelf, row,col):
        return shelf.tmap[row][col]
    
    def can_move(shelf,pos) -> bool:
        if pos[0]>= 0 and pos[1] >= 0 and pos[0] < shelf.HEIGHT and pos[1] < shelf.WIDTH:
            return shelf.tmap[pos[0]][pos[1]][0] == 'e'
        else:
            return False

    def shortest(shelf, start, finish):
        vistited = {start}
        q = [(start,0)]
        steps = -1
        while q and steps < 0:
            (current,s) = q.pop(0)
            if current == finish:
                steps = s
            else:
                s+=1
                up = (current[0]-1,current[1])
                if shelf.can_move(up):
                    if not up in vistited:
                        vistited.add(up)
                        q.append((up,s))
                down = (current[0]+1,current[1])
                if shelf.can_move(down):
                    if not down in vistited:
                        vistited.add(down)
                        q.append((down,s))
                left = (current[0],current[1]-1)
                if shelf.can_move(left):
                    if not left in vistited:
                        vistited.add(left)
                        q.append((left,s))
                right = (current[0],current[1]+1)
                if shelf.can_move(right):
                    if not right in vistited:
                        vistited.add(right)
                        q.append((right,s))
        return steps
    
def main():
    print("hello")
    ocean= Ocean()
    ocean.print()
    row = ocean.HEIGHT
    print(ocean.shortest((1,1),(2,2)))

if __name__ == "__main__":
    main()