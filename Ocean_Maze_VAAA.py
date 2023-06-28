"""
'Title: ocean Maze'
Author: Bailey Reid
Date: 29/07/22
Version: 0.32
Purpose: to lick me
https://tkdocs.com/tutorial/index.html
"""
from tkinter import Tk, NW, Canvas, Frame, Button, PhotoImage, Menu
import tkinter.simpledialog as Tksm
import sys
import random
import os, sys
import pathlib
from time import sleep
sys.path.insert(0,"Gen")

import ACC 
import Pick

potato = ["1potato","2baked_potato","3poisonous_potato","OceanMan"]

class GameGUI():

    assetsone = False
    are_move = False
    cheese = 0
    
    # Draw Maze {Blue}
    def draw(self, canvas):
        """
        the draw map method"""
        canvas.delete('all')
        for row in range(self.ocean.HEIGHT):
            for col in range(self.ocean.WIDTH):
                if "e" in self.ocean.get(row,col):
                    dub = self.ocean.get(row,col)
                    if self.assetsone == True:
                        canvas.create_image((col * 32)+2, (row * 32)+2, image=self.emg_vault[dub], anchor=NW)
                    else:
                        canvas.create_image((col * 32)+2, (row * 32)+2, image=self.img_eault[dub], anchor=NW)
                #
                elif "w" in self.ocean.get(row,col):
                    dub = self.ocean.get(row,col)
                    if self.assetsone == True:
                        canvas.create_image((col * 32)+2, (row * 32)+2, image=self.wmg_vault[dub], anchor=NW)
                    else:
                        canvas.create_image((col * 32)+2, (row * 32)+2, image=self.img_wault[dub], anchor=NW)
                
                else:
                    print("Idfk Man")
            canvas.create_image(self.Stoot.col*32,self.Stoot.row*32,image = self.stootimg,anchor=NW)
            canvas.create_image(self.End.col*32,self.End.row*32,image = self.endimg,anchor=NW)
            canvas.create_image(self.Picker.col*32,self.Picker.row*32,image = self.pickerimg,anchor=NW)
    
    def canvas_draw(self):
        self.maze_canvas.grid_forget()
        self.maze_canvas = Canvas(self.frame, bg='#ffcfdc', height=self.ocean.HEIGHT * 32, width=self.ocean.WIDTH * 32)
        self.maze_canvas.grid(row=0, column=0)
        self.draw(self.maze_canvas)

    def move(self,x,y):
        self.Picker.move(x,y,self.ocean)
        self.draw(self.maze_canvas)

    def __init__(self,master):
        
        """the initiate method imports images"""
        self.frame = Frame(master, bg='#ffcfdc')
        self.frame.pack()
        self.ocean = ACC.Ocean()
        self.tmap = ACC.Ocean.tmap
        # Set up imagesh here and peenis
        self.Picker = Pick.Pick("Picker",self.ocean.XY,self.ocean.XR)
        self.Stoot = Pick.Pick("Start",self.ocean.XY,self.ocean.XR)
        self.End = Pick.Pick("End",self.ocean.YY,self.ocean.YR)

        starto = random.choice(potato)
        if starto == "OceanMan":
            yep = "Ocean Man Take Me By The Hand"
        else:
            yep = "Lmao Maze Checking Systemm"
        self.pickerimg = PhotoImage(file=(f"./Assets/{starto}.png"))
        self.stootimg = PhotoImage(file=(f"./Assets/FloodStart.png"))
        self.endimg = PhotoImage(file=(f"./Assets/FloodEnd.png"))
        
        ##red Image Vault's
        self.img_wault = {"w":PhotoImage(file=("./Assets/W.png")),"wa":PhotoImage(file=("./Assets/A.png")),"wb":PhotoImage(file=("./Assets/B.png")),"wc":PhotoImage(file=("./Assets/C.png")),"wd":PhotoImage(file=("./Assets/D.png")),"wg":PhotoImage(file=("./Assets/G.png")),"wi":PhotoImage(file=("./Assets/I.png")),"wj":PhotoImage(file=("./Assets/J.png")),"wl":PhotoImage(file=("./Assets/L.png")),"wn":PhotoImage(file=("./Assets/N.png")),"wp":PhotoImage(file=("./Assets/P.png")),"wq":PhotoImage(file=("./Assets/Q.png")),"wr":PhotoImage(file=("./Assets/R.png")),"ws":PhotoImage(file=("./Assets/S.png")),"wt":PhotoImage(file=("./Assets/T.png")),"wu":PhotoImage(file=("./Assets/U.png")),"wx":PhotoImage(file=("./Assets/X.png"))}
        self.img_eault = {"e":PhotoImage(file=("./Assets/E.png")),"ea":PhotoImage(file=("./Assets/E.png")),"eb":PhotoImage(file=("./Assets/E.png")),"ec":PhotoImage(file=("./Assets/E.png")),"ed":PhotoImage(file=("./Assets/E.png")),"eg":PhotoImage(file=("./Assets/E.png")),"ei":PhotoImage(file=("./Assets/E.png")),"ej":PhotoImage(file=("./Assets/E.png")),"el":PhotoImage(file=("./Assets/E.png")),"en":PhotoImage(file=("./Assets/E.png")),"ep":PhotoImage(file=("./Assets/E.png")),"eq":PhotoImage(file=("./Assets/E.png")),"er":PhotoImage(file=("./Assets/E.png")),"es":PhotoImage(file=("./Assets/E.png")),"et":PhotoImage(file=("./Assets/E.png")),"eu":PhotoImage(file=("./Assets/E.png")),"ex":PhotoImage(file=("./Assets/E.png"))}
        self.wmg_vault = {"w":PhotoImage(file=("./Wssets/W.png")),"wa":PhotoImage(file=("./Wssets/A.png")),"wb":PhotoImage(file=("./Wssets/B.png")),"wc":PhotoImage(file=("./Wssets/C.png")),"wd":PhotoImage(file=("./Wssets/D.png")),"wg":PhotoImage(file=("./Wssets/G.png")),"wi":PhotoImage(file=("./Wssets/I.png")),"wj":PhotoImage(file=("./Wssets/J.png")),"wl":PhotoImage(file=("./Wssets/L.png")),"wn":PhotoImage(file=("./Wssets/N.png")),"wp":PhotoImage(file=("./Wssets/P.png")),"wq":PhotoImage(file=("./Wssets/Q.png")),"wr":PhotoImage(file=("./Wssets/R.png")),"ws":PhotoImage(file=("./Wssets/S.png")),"wt":PhotoImage(file=("./Wssets/T.png")),"wu":PhotoImage(file=("./Wssets/U.png")),"wx":PhotoImage(file=("./Wssets/X.png"))}
        self.emg_vault = {"e":PhotoImage(file=("./Essets/E.png")),"ea":PhotoImage(file=("./Essets/E.png")),"eb":PhotoImage(file=("./Essets/EB.png")),"ec":PhotoImage(file=("./Essets/EC.png")),"ed":PhotoImage(file=("./Essets/ED.png")),"eg":PhotoImage(file=("./Essets/EG.png")),"ei":PhotoImage(file=("./Essets/EI.png")),"ej":PhotoImage(file=("./Essets/EJ.png")),"el":PhotoImage(file=("./Essets/EL.png")),"en":PhotoImage(file=("./Essets/EN.png")),"ep":PhotoImage(file=("./Essets/EP.png")),"eq":PhotoImage(file=("./Essets/EQ.png")),"er":PhotoImage(file=("./Essets/ER.png")),"es":PhotoImage(file=("./Essets/ES.png")),"et":PhotoImage(file=("./Essets/ET.png")),"eu":PhotoImage(file=("./Essets/EU.png")),"ex":PhotoImage(file=("./Essets/EX.png"))}
        ##
        
        # set up canvas for map
        self.maze_canvas = Canvas(self.frame, bg='#ffcfdc', height=self.ocean.HEIGHT * 32, width=self.ocean.WIDTH * 32)
        self.maze_canvas.grid(row=1, column=0, columnspan=3, rowspan=3)
        self.draw(self.maze_canvas)
    
        # set title of window
        self.frame.master.wm_title(yep)
        self.frame.master.wm_iconbitmap(pathlib.Path(f"./Assets/{starto}.ico"))
        #self.frame.master.wm_iconbitmap(pathlib.Path("./Assets/Boris.ico"))

        master.bind('w', lambda event: self.UMove())
        master.bind('s', lambda event: self.DMove())
        master.bind('a', lambda event: self.LMove())
        master.bind('d', lambda event: self.RMove())

        master.bind('<space>', lambda event: self.checkerint())

        master.bind('P', lambda event: self.printtmap())
        
        self.boU = Button(self.frame, text="Check Selected Tile", command=self.checkerint, bg='#ffcfdc')
        self.boU.grid(row=20, column=1)

        self.boB = Button(self.frame, text="Check All Tiles", command=self.checkall, bg='#ffcfdc')
        self.boB.grid(row=32, column=1)

        self.bobatea = Button(self.frame, text="Regenerate Maze", command=self.regenlololol, bg='#ffcfdc')
        self.bobatea.grid(row=32, column=0)

        self.switch = Button(self.frame, text="Switch Assets", command=self.switchassets, bg='#ffcfdc')
        self.switch.grid(row=32, column=2)

        self.pizza = Button(self.frame, text="Pizza Text", command=self.cheese_roll, bg='#ffcfdc')
        self.pizza.grid(row=20, column=2)
        
        
        self.menubar = Menu(self.frame)
        self.frame.master.config(menu=self.menubar,bg='#ffcfdc')
        
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Restart",command=lambda: self.Restart())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="OpenMaze",command=lambda: self.openmaze())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.frame.master.destroy)

        self.menubar.add_cascade(label="File",menu=self.filemenu)

    def switchassets(self):
        ##blue True → False
        if self.assetsone == True:
            self.assetsone = False
            
            tato = random.choice(potato)
            if tato == "OceanMan":
                pey = "Ocean Man Take Me By The Hand"
            else:
                pey = "Lmao Maze Checking Systemm"
            self.pickerimg = PhotoImage(file=(f"./Assets/{tato}.png"))
            self.frame.master.wm_title(pey)
            self.frame.master.wm_iconbitmap(pathlib.Path(f"./Assets/{tato}.ico"))
            
            self.draw(self.maze_canvas)
        ##
        
        ##yellow False → True
        elif self.assetsone == False:
            self.assetsone = True
            
            tato = random.choice(potato)
            if tato == "OceanMan":
                pey = "Ocean Man Take Me By The Hand"
            else:
                pey = "Lmao Maze Checking Systemm"
            self.pickerimg = PhotoImage(file=(f"./Assets/{tato}.png"))
            self.frame.master.wm_title(pey)
            self.frame.master.wm_iconbitmap(pathlib.Path(f"./Assets/{tato}.ico"))
            
            self.draw(self.maze_canvas)
        ##

    # Recreate/Change Stuff {red,22}
    def regenlololol(self):
        self.ocean.regen()
        self.Picker.restartS(self.ocean.XY,self.ocean.XR)
        self.Stoot.restartS(self.ocean.XY,self.ocean.XR)
        self.End.restartS(self.ocean.YY,self.ocean.YR)
        self.draw(self.maze_canvas)
        self.ocean.print()
    

    ##green Checking System
    def checkerint(self):
        rowa = self.Picker.row
        cola = self.Picker.col
        self.ocean.changenabor(rowa,cola)
        self.draw(self.maze_canvas)

    def checkall(self):
        rowa = 0
        cola = 0
        for x in range(self.ocean.WIDTH):
            for y in range(self.ocean.HEIGHT):
                self.ocean.changenabor(rowa,cola)
                rowa+=1
            cola+=1
            rowa = 0
        self.draw(self.maze_canvas)
    ##

    def Restart(self):
        """Module for restarting the game once the player has either won or decided to restart via the file menu"""
        self.Picker.restartS(0,7)
        self.draw(self.maze_canvas)

    


    def openmaze(self):
        self.ocean.loadm ()
        self.Picker.restartS(self.ocean.XY,self.ocean.XR)
        self.Stoot.restartS(self.ocean.XY,self.ocean.XR)
        self.End.restartS(self.ocean.YY,self.ocean.YR)
        self.canvas_draw()

    ##red Movement System
    def UMove(self):
        self.move("up",1)

    def DMove(self):
        self.move("down",1)

    def LMove(self):
        self.move("left",1)

    def RMove(self):
        self.move("right",1)
    ##

    def cheese_roll(self):
        cheesing_time = random.choice(potato)
        if cheesing_time == "OceanMan":
            pey = "Ocean Man Take Me By The Hand"
        else:
            pey = "Lmao Maze Checking Systemm"
        self.frame.master.wm_title(pey)
        self.pickerimg = PhotoImage(file=(f"./Assets/{cheesing_time}.png"))
        self.frame.master.wm_iconbitmap(pathlib.Path(f"./Assets/{cheesing_time}.ico"))
        self.draw(self.maze_canvas)
        self.pizza.after(200, self.cheese_roll)

    def printtmap(self):
        self.ocean.printtmap()
    
root = Tk()
root.configure(bg='#ffcfdc')
abc = GameGUI(root)
root.mainloop()
##36FF00
