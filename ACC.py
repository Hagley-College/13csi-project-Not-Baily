from clrprint import *
import tkinter as tl
from tkinter import filedialog as fd
import sys, copy
import Random_Maze as RT
has = False
First_trigger = False


filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
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

        YY = 19
        XR, XY, YR = int(line_start[0]), int(line_start[1]), int(line_start[2]) 
        WIDTH, HEIGHT = int(line_size[0]), int(line_size[1]) 
        return tmap,XR,XY,YR,YY,WIDTH,HEIGHT


    mazesele = input("Do you want to use a random maze, the default or open your own? (random(1), default(2) or file(3))\n")
    
    if mazesele == '2' or mazesele == 'default':
        tmap = [['w','w','w','w','w','w','w','e','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','e','w','e','e','e','e','e','w','e','e','e','e','e','e','e','e','e','e','w'],
['w','e','e','e','w','w','w','w','w','e','w','w','w','e','w','w','w','w','e','w'],
['w','w','w','e','w','e','e','e','e','e','w','e','w','e','w','e','w','w','e','w'],
['w','e','w','e','e','e','w','w','w','w','w','e','w','e','w','e','e','e','e','w'],
['w','e','w','w','w','w','w','e','e','e','e','e','w','e','e','w','e','w','e','w'],
['w','e','w','e','e','w','w','e','w','w','w','e','w','e','w','e','e','w','e','w'],
['w','e','e','e','w','e','w','e','w','e','e','e','w','e','w','e','w','e','e','w'],
['w','e','w','e','e','e','w','e','w','e','w','w','w','e','w','e','w','e','w','w'],
['w','e','w','w','w','e','e','e','w','e','e','e','e','e','w','e','w','e','e','w'],
['w','e','e','e','e','w','w','w','w','w','w','w','w','w','e','e','w','e','e','w'],
['w','w','e','w','e','w','e','e','e','e','e','e','e','w','e','w','e','e','e','w'],
['w','e','e','w','e','w','w','e','w','e','w','w','e','w','e','w','e','w','w','w'],
['w','e','e','w','e','e','e','e','w','w','e','e','e','e','e','w','e','w','e','w'],
['w','w','e','w','w','w','w','w','w','e','w','w','e','w','w','w','e','w','e','w'],
['w','e','e','e','w','w','e','w','e','e','e','e','w','e','e','e','e','w','e','w'],
['w','w','w','e','e','e','e','w','e','w','w','e','e','e','w','w','w','e','e','w'],
['w','e','w','e','w','w','e','w','e','e','w','w','w','w','e','e','e','e','e','w'],
['w','e','e','e','w','e','e','w','w','e','e','e','e','e','e','w','e','w','e','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','e','w']]
        XR = 7
        XY = 0
        YR = 18
        YY = 19
        WIDTH = 20
        HEIGHT = 20
        print(f'\nMaze Height = {HEIGHT}\nMaze Width = {WIDTH}')
    elif mazesele == '1' or mazesele == 'random':
        tmap,XR,YR,WIDTH,HEIGHT = RT.GenerateMate()
        XY = 0
        YY = 19
        print(f'\nMaze Height = {HEIGHT}\nMaze Width = {WIDTH}')
    elif mazesele == '3' or mazesele == 'file':
        tmap,XR,XY,YR,YY,WIDTH,HEIGHT = loadm()
        print(f'\nMaze Height = {HEIGHT}\nMaze Width = {WIDTH}')
    elif mazesele == "4":
        import NotStolenMazeGen
        tmap = NotStolenMazeGen.maze
        WIDTH = NotStolenMazeGen.width
        HEIGHT = NotStolenMazeGen.height
        XR = 1
        XY = 0
        YR = 18
        YY = 19
    else:
        print("invalid option setting to default maze")
        tmap = [['w','w','w','w','w','w','w','e','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','e','w','e','e','e','e','e','w','e','e','e','e','e','e','e','e','e','e','w'],
['w','e','e','e','w','w','w','w','w','e','w','w','w','e','w','w','w','w','e','w'],
['w','w','w','e','w','e','e','e','e','e','w','e','w','e','w','e','w','w','e','w'],
['w','e','w','e','e','e','w','w','w','w','w','e','w','e','w','e','e','e','e','w'],
['w','e','w','w','w','w','w','e','e','e','e','e','w','e','e','w','e','w','e','w'],
['w','e','w','e','e','w','w','e','w','w','w','e','w','e','w','e','e','w','e','w'],
['w','e','e','e','w','e','w','e','w','e','e','e','w','e','w','e','w','e','e','w'],
['w','e','w','e','e','e','w','e','w','e','w','w','w','e','w','e','w','e','w','w'],
['w','e','w','w','w','e','e','e','w','e','e','e','e','e','w','e','w','e','e','w'],
['w','e','e','e','e','w','w','w','w','w','w','w','w','w','e','e','w','e','e','w'],
['w','w','e','w','e','w','e','e','e','e','e','e','e','w','e','w','e','e','e','w'],
['w','e','e','w','e','w','w','e','w','e','w','w','e','w','e','w','e','w','w','w'],
['w','e','e','w','e','e','e','e','w','w','e','e','e','e','e','w','e','w','e','w'],
['w','w','e','w','w','w','w','w','w','e','w','w','e','w','w','w','e','w','e','w'],
['w','e','e','e','w','w','e','w','e','e','e','e','w','e','e','e','e','w','e','w'],
['w','w','w','e','e','e','e','w','e','w','w','e','e','e','w','w','w','e','e','w'],
['w','e','w','e','w','w','e','w','e','e','w','w','w','w','e','e','e','e','e','w'],
['w','e','e','e','w','e','e','w','w','e','e','e','e','e','e','w','e','w','e','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','e','w']]
        XR = 7
        XY = 0
        YR = 18
        YY = 19
        WIDTH = 20
        HEIGHT = 20
        print(f'\nMaze Height = {HEIGHT}\nMaze Width = {WIDTH}')

#Col = Left/Right = cola
#Row = Up/Down = rowa
    

    def print(self):
        for row in self.tmap:
            for col in row:
                print(col,end ='')
            print()
    def printtmap(self):
        for x in range(self.HEIGHT):
            print(self.tmap[x])
    def get(self,row,col):
        return self.tmap[row][col]
    
    def regen(self):
        self.tmap,self.XR,self.YR,self.WIDTH,self.HEIGHT = RT.GenerateMate()
        self.XY = 0
        self.YY = 19
    
    def opendif(self):
        self.tmap,self.XR,self.XY,self.YR,self.YY,self.WIDTH,self.HEIGHT = self.loadm()

    def changenabor(self,rowa,cola):
        #HEIGHT = self.HEIGHT
        #WIDTH = self.WIDTH
        
        if rowa == None:
            rowa = 0
        elif rowa > self.HEIGHT-1:
            rowa = self.HEIGHT-1
        
        if cola == None:
            cola = 0
        elif cola > self.WIDTH-1:
            cola = self.WIDTH-1
        
        wd = False
        wu = False
        wr = False
        wl = False

        ed = False
        eu = False
        el = False
        er = False

        #rowa = rowa-1
        #cola = cola-1
        # Checker {white, 49}
        if "w" in self.tmap[rowa][cola]:
            print('\nW = True')
            
            ##red
            # Down {red, 9}
            if rowa < self.HEIGHT-1:
                if "w" in self.tmap[rowa+1][cola]:
                    wd = True
                    print("Down W = True")
                else:
                    wd = False
                    print("\nDown W = False")
            else:
                wd = False
            ##
            
            ##blue
            # Up {blue, 10}
            if rowa > 0:
                if "w" in self.tmap[rowa-1][cola]:
                    wu = True
                    print("Up W = True")
                else:
                    wu = False
                    print("\nUp W = False")
            
            else:
                wu = False
            ##

            ##green
            # Right {green, 10}
            if cola < self.WIDTH-1:
                if "w" in self.tmap[rowa][cola+1]:
                    wr = True
                    print("Right W = True")
                
                else:
                    wr = False
                    print("\nRight W = False")
            else:
                wr = False
            ##

            ##yellow
            # Left {yellow, 10}
            if cola > 0:
                if "w" in self.tmap[rowa][cola-1]:
                    wl = True
                    print("Left W = True")
                
                else:
                    wl = False
                    print("\nLeft W = False")             
            else:
                wl = False
            ##
        
        
        elif "e" in self.tmap[rowa][cola]:
            print("\nE = True")
            ##red
            # Down {red, 9}
            if rowa < self.HEIGHT-1:
                if "e" in self.tmap[rowa+1][cola]:
                    ed = True
                    print("Down E = True")
                else:
                    ed = False
                    print("\nDown E = False")
            else:
                ed = False
            ##
            
            ##blue
            # Up {blue, 10}
            if rowa > 0:
                if "e" in self.tmap[rowa-1][cola]:
                    eu = True
                    print("Up E = True")
                else:
                    eu = False
                    print("\nUp E = False")
            else:
                eu = False
            ##

            ##green
            # Right {green, 10}
            if cola < self.WIDTH-1:
                if "e" in self.tmap[rowa][cola+1]:
                    er = True
                    print("Right E = True")
                
                else:
                    er = False
                    print("\nRight E = False")
            else:
                er = False
            ##

            ##yellow
            # Left {yellow, 10}
            if cola > 0:
                if "e" in self.tmap[rowa][cola-1]:
                    el = True
                    print("Left E = True")
                
                else:
                    el = False
                    print("\nLeft E = False")             
            else:
                el = False
            ##
        else:
            print("Error Nothing Found")

        ##red WWWWWWWWWWWW
        #Misc
        if wd and wu and wr and wl == True:
            self.tmap[rowa][cola] = 'wa'
            print("\nAll = True  WA")
        
        elif wd and wu and wr == True:
            self.tmap[rowa][cola] = 'wx'
            print("Down, Up and Right = True  WX\n")
        
        elif wd and wu and wl == True:
            self.tmap[rowa][cola] = 'wi'
            print("Down, Up and Right = True  WI\n")
        
        elif wd and wl and wr == True:
            self.tmap[rowa][cola] = 'wp'
            print("Down, Left and Right = True  WP\n")
        
        elif wu and wl and wr == True:
            self.tmap[rowa][cola] = 'wq'
            print("Up, Left and Right = True  WQ\n")  

        #Down W
        elif wd and wu == True:
            self.tmap[rowa][cola] = 'wg'
            print("Down And Up = True  WG\n")
        
        
        elif wd and wr == True:
            self.tmap[rowa][cola] = 'wb'
            print("Down And Right = True  WB\n")
        
        elif wd and wl == True:
            self.tmap[rowa][cola] = 'ws'
            print("Down and Left = True  WF\n")
        
        elif wd == True:
            self.tmap[rowa][cola] = 'wd'
            print("Down = True  WD\n")
        
        # Up W
        elif wu and wr == True:
            self.tmap[rowa][cola] = 'wc'
            print("Up And Right = True  WC\n")
        
        elif wu and wl == True:
            self.tmap[rowa][cola] = 'wj'
            print("Up And Left = True  WJ\n")
        
        elif wu == True:
            self.tmap[rowa][cola] = 'wu'
            print("Up = True  WU\n")

        #Left And Right W
        elif wr and wl == True:
            self.tmap[rowa][cola] = 'wt'
            print("Right And Left = True WT\n")
        
        elif wr == True:
            self.tmap[rowa][cola] = 'wr'
            print("Right = True  WR\n")
        
        elif wl == True:
            self.tmap[rowa][cola] = 'wl'
            print("Left = True  WL\n")
        
        else:
            self.tmap[rowa][cola] = 'wn'
            print("\nAll = False  WN\n")
        ##

        ##blue EEEEEEEEEEEEEEEEEEEEEEEEEEEEE
        #Misc
        if ed and eu and er and el == True:
            self.tmap[rowa][cola] = 'ea'
            print("\nAll E = True  EA")
        
        elif ed and eu and er == True:
            self.tmap[rowa][cola] = 'ex'
            print("Down, Up and Right E = True  EX\n")
        
        elif ed and eu and el == True:
            self.tmap[rowa][cola] = 'ei'
            print("Down, Up and Right E = True  EI\n")
        
        elif ed and el and er == True:
            self.tmap[rowa][cola] = 'ep'
            print("Down, Left and Right E = True  EP\n")
        
        elif eu and el and er == True:
            self.tmap[rowa][cola] = 'eq'
            print("Up, Left and Right E = True  EQ\n")
        
        #Down E
        elif ed and eu == True:
            self.tmap[rowa][cola] = 'eg'
            print("Down And Up E = True  EG\n")
        
        elif ed and er == True:
            self.tmap[rowa][cola] = 'eb'
            print("Down And Right E = True  EB\n")
        
        elif ed and el == True:
            self.tmap[rowa][cola] = 'es'
            print("Down and Left E = True  EF\n")
        
        elif ed == True:
            self.tmap[rowa][cola] = 'ed'
            print("Down E = True  ED\n")

        #Up E
        elif eu and er == True:
            self.tmap[rowa][cola] = 'ec'
            print("Up And Right E = True EC\n")
        
        elif eu and el == True:
            self.tmap[rowa][cola] = 'ej'
            print("Up And Left E = True EJ\n")
        
        elif eu == True:
            self.tmap[rowa][cola] = 'eu'
            print("Up E = True EU\n")

        #Left and Right E
        elif er and el == True:
            self.tmap[rowa][cola] = 'et'
            print("Right And Left E = True ET\n")
        
        elif er == True:
            self.tmap[rowa][cola] = 'er'
            print("Right E = True ER\n")
        
        elif el == True:
            self.tmap[rowa][cola] = 'el'
            print("Left E = True EL\n")
        
        else:
            print("\nAll E = False\n")
        ##
        print(f"height = {self.HEIGHT}, width = {self.WIDTH}\n")
        return self.tmap

