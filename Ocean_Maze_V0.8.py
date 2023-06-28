"""
'Title: Ocean Maze'
Author: Bailey Reid
Date: 29/07/22
Version: 0.8
Purpose:
https://tkdocs.com/tutorial/index.html
"""
from tkinter import Tk, NW, Canvas, StringVar, Frame, Button, Label, PhotoImage, Menu, Text, messagebox, Toplevel  # import Tk (Tcl/Tk) Interface,
import tkinter.simpledialog as Tksm
import sys
import random
import sys

import pathlib
sys.path.insert(0,"Maze_Generation_Modules")

import Swim
import Ocean

#Enables Debug Mode Which Unlocks Tools To Help Finding Bugs (True = Debug Mode on, False = Debug Mode off)
DebugMode = True

evom_step = 1
bag_sttep = 0
bagcanmove = False

error_has = False
HasWon = False


#Asks if the player wants buttons to be enabled
movesys = messagebox.askquestion(message='Do You Want To Be Able To Use Buttons?',icon='question', title='Maze Setup')
if movesys == 'yes':
    AreButtons = True
else:
    AreButtons = False

class GameGUI():
    """
    The GameGUI class contains a Frame so we can add buttons when it is initiated it receives a Graphical user interface
    tool kit
    tk as an argument.
    """



    def WinPop(self):
        """This is the win screen system so when you get to the goal at the end of the maze"""
        #Col = Left/Right
        #Row = Up/Down
        win = Toplevel()
        win.title('You Win!!!!')

        def rvw():
            """Function to allow the restart button on the win screen to work because I couldn't figure out how to run two command on a button without using a function"""
            self.Restart()
            win.destroy()

        message = "Congrats you've gotten the bag so you win!"
        lablab = Label(win, text=message)
        lablab.grid(column=2,row=0)

        bto = Button(win, text="Restart",command=rvw)
        bto.grid(column=1,row=1)

        btt = Button(win, text="Get this message outa my face",command=win.destroy)
        btt.grid(column=2,row=1)

        btth = Button(win, text="Exit",command=self.frame.master.destroy)
        btth.grid(column=3,row=1)

    def bag_colosion(self):
        """This is what happens when the bag hits the player instad of the player hitting the bag"""
        print('Exception in Bag callback\nTraceback (most recent call last):\n  File "Ocean_Maze_V0.8.py", line ∞, in <collision>\n    if Swim.Sprite.hit(self,self.boris,self.bag):\nUnexpectedError: "You are not supposed to hit the player with the bag"')


    def draw(self, canvas):
        """
        the draw map method"""
        canvas.delete('all')
        for row in range(self.ocean.HEIGHT):
            for col in range(self.ocean.WIDTH):
                if "e" in self.ocean.get(row,col):
                    dub = self.ocean.get(row,col)
                    canvas.create_image((col * 32)+2, (row * 32)+2, image=self.emg_vault[dub], anchor=NW)
                #
                elif "w" in self.ocean.get(row,col):
                    dub = self.ocean.get(row,col)
                    canvas.create_image((col * 32)+2, (row * 32)+2, image=self.wmg_vault[dub], anchor=NW)

                else:
                    print("Idfk Man")
            canvas.create_image(self.bag.col*32,self.bag.row*32,image = self.BagImg,anchor=NW)
            #canvas.create_image(self.End.col*32,self.End.row*32,image = self.endimg,anchor=NW)
            canvas.create_image(self.boris.col*32,self.boris.row*32,image = self.BorisImg,anchor=NW)

    def move(self,x,y):
        """Both the movement system and the win colision system for Boris"""
        global HasWon
        self.boris.move(x,y,self.ocean)
        self.draw(self.maze_canvas)
        if HasWon == False:
            if Swim.Sprite.hit(self,self.boris,self.bag):
                print("You Win!!!")
                self.WinPop()
                HasWon = True
        else:
            None

    def moveBag(self,x,y):
        """Both the movement system and the colision system for the Bag (Goal)"""
        global error_has
        self.bag.move(x,y,self.ocean)
        self.draw(self.maze_canvas)
        if error_has == False:
            if Swim.Sprite.hit(self,self.boris,self.bag):
                self.bag_colosion()
                error_has = True
        else:
            None

    def __init__(self,master):
        
        
        def nothinghere(event):
            """Function that's used as a placeholder for when a function isn't yet created"""
            print(event)

        
        """the initiate method imports images"""
        self.frame = Frame(master)
        self.frame.pack()
        self.ocean = Ocean.Ocean()
        self.boris = Swim.Sprite("Boris",0,7)
        self.bag = Swim.Sprite("Bag",19,18)
        print(f'\nMaze Height = {self.ocean.HEIGHT}\nMaze Width = {self.ocean.WIDTH}')
        # Set up images
        self.wmg_vault = {"w":PhotoImage(file=("./Wssets/W.png")),"wa":PhotoImage(file=("./Wssets/A.png")),"wb":PhotoImage(file=("./Wssets/B.png")),"wc":PhotoImage(file=("./Wssets/C.png")),"wd":PhotoImage(file=("./Wssets/D.png")),"wg":PhotoImage(file=("./Wssets/G.png")),"wi":PhotoImage(file=("./Wssets/I.png")),"wj":PhotoImage(file=("./Wssets/J.png")),"wl":PhotoImage(file=("./Wssets/L.png")),"wn":PhotoImage(file=("./Wssets/N.png")),"wp":PhotoImage(file=("./Wssets/P.png")),"wq":PhotoImage(file=("./Wssets/Q.png")),"wr":PhotoImage(file=("./Wssets/R.png")),"ws":PhotoImage(file=("./Wssets/S.png")),"wt":PhotoImage(file=("./Wssets/T.png")),"wu":PhotoImage(file=("./Wssets/U.png")),"wx":PhotoImage(file=("./Wssets/X.png"))}
        self.emg_vault = {"e":PhotoImage(file=("./Essets/E.png")),"ea":PhotoImage(file=("./Essets/E.png")),"eb":PhotoImage(file=("./Essets/EB.png")),"ec":PhotoImage(file=("./Essets/EC.png")),"ed":PhotoImage(file=("./Essets/ED.png")),"eg":PhotoImage(file=("./Essets/EG.png")),"ei":PhotoImage(file=("./Essets/EI.png")),"ej":PhotoImage(file=("./Essets/EJ.png")),"el":PhotoImage(file=("./Essets/EL.png")),"en":PhotoImage(file=("./Essets/EN.png")),"ep":PhotoImage(file=("./Essets/EP.png")),"eq":PhotoImage(file=("./Essets/EQ.png")),"er":PhotoImage(file=("./Essets/ER.png")),"es":PhotoImage(file=("./Essets/ES.png")),"et":PhotoImage(file=("./Essets/ET.png")),"eu":PhotoImage(file=("./Essets/EU.png")),"ex":PhotoImage(file=("./Essets/EX.png"))}
        self.BorisImg = PhotoImage(file=pathlib.Path("./Assets/Boris_32x32.png"))
        self.BagImg = PhotoImage(file=pathlib.Path("./Assets/Bag_32x32.png"))
        # set up canvas for map
        self.maze_canvas = Canvas(self.frame, bg='#ffffff', height=self.ocean.HEIGHT * 32, width=self.ocean.WIDTH * 32)
        self.maze_canvas.grid(row=1, column=0, columnspan=3, rowspan=3)
        self.draw(self.maze_canvas)

        # set title of window
        self.frame.master.wm_title('Lmao Maze')
        self.frame.master.wm_iconbitmap(pathlib.Path("./Assets/Boris.ico"))




        
        ##Menu Bars
        ##ff0000 

        #Adds all the menu bars that sit on the top of the screen when playing
        self.menubar = Menu(self.frame)
        self.frame.master.config(menu=self.menubar)
        
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Restart",command=lambda: self.Restart())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.frame.master.destroy)

        self.menubar.add_cascade(label="File",menu=self.filemenu)
    
        
        self.helpmenu = Menu(self.menubar,tearoff=0)
        
        self.helpmenu.add_command(label="Help",command=self.HelpMenu)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About",command=self.About)
        
        self.menubar.add_cascade(label="About",menu=self.helpmenu)

        
        self.configmenu = Menu(self.menubar,tearoff=0)

        self.configmenu.add_command(label="Movable Bag Toggle",command=self.BagMoveSet)
       
        self.menubar.add_cascade(label="Config",menu=self.configmenu)

        if DebugMode == True:
            #All the debug options for when debug move is turned on
            self.debugmenu = Menu(self.menubar,tearoff=0)
            self.debugmenu.add_command(label="Print Info",command=self.debug_print)
            self.debugmenu.add_separator()
            self.debugmenu.add_command(label="Select Move Character",command=self.debug_move)
            self.debugmenu.add_separator()
            self.debugmenu.add_command(label="Move Per Step",command=self.Move_Step)
            self.debugmenu.add_separator()

            
            self.debugmenu.add_command(label="Call Function",command=self.debug_funct)

            self.menubar.add_cascade(label="Debug",menu=self.debugmenu)



        self.frame.master['menu'] = self.menubar

    
        ##Buttons
        
        if AreButtons == True:
            """Method of placing buttons on the window if option "yes" is picked"""
            print('\nOption Yes Was Picked For Buttons, Placing Buttons\n')

            self.boU = Button(self.frame, text="Up", command=self.UMove)
            self.boU.grid(row=20, column=1)

            
            self.boL = Button(self.frame, text="Left", command=self.LMove)
            self.boL.grid(row=21, column=0)
        

            self.boD = Button(self.frame, text="Down", command=self.DMove)
            self.boD.grid(row=22, column=1)

            self.boR = Button(self.frame, text="Right", command=self.RMove)
            self.boR.grid(row=21, column=2)

        #Keybinds
        #fa6665 
        
        #Binds keybinds to the movement system to be able to move with WASD
        master.bind('w', lambda event: self.UMove())
        master.bind('s', lambda event: self.DMove())
        master.bind('a', lambda event: self.LMove())
        master.bind('d', lambda event: self.RMove())
        master.bind('<Escape>', lambda event: self.frame.master.destroy())
        

        #Bag Keybinds
        
        
        #The same as the other keybinds but allows the Bag (Goal) to be moved with UJHK instead
        master.bind('u', lambda event: self.UMoveB())
        master.bind('j', lambda event: self.DMoveB())
        master.bind('h', lambda event: self.LMoveB())
        master.bind('k', lambda event: self.RMoveB())


    #Menu Bar Functions
    
    def Restart(self):
        """Module for restarting the game once the player has either won or decided to restart via the file menu"""
        global HasWon
        self.boris.restartS(0,7)
        self.bag.restartS(19,18)
        self.draw(self.maze_canvas)
        HasWon = False

    def About(self):
        """Module for displaying infomation about the maze game thing"""
        messagebox.showinfo('About', "Title: Ocean Maze\nAuthor: Bailey Reid\nVersion: 0.8\nAn attempt to create a somewhat interesting maze")

    def HelpMenu(self):
        """Explains how to play the game and what your objective is"""
        if AreButtons == True:
            messagebox.showinfo('Help', 'Your main goal is to reach the bag at the other end of the maze, touching it will make you win.\n\nYou have two movement options WASD and the buttons at the bottem of your screen.\n\nWASD are four keys on the keyboard that coraspond to the four directions you can move Up(W), Down(S), Left(L) and Right(D).\n\nThe Buttons are arrange in a way to make it easy to tell which direction they coraspond to, for exaample the button on top moves the character up.\n\nIf you go to config and turn on the "Movable Bag Toggle" it will enable you to move the bag as well (the controlls are differnt for the bag: U=Up, H=Right, L=Left and J=Down)')
        else:
            messagebox.showinfo('Help', 'Your main goal is to reach the bag at the other end of the maze, touching it will make you win.\n\nThe way to controll the character on screen is using WASD\nWASD are four keys on the keyboard that coraspond to the four directions you can move Up(W), Down(S), Left(L) and Right(D).\n\nIf you go to config and turn on the "Movable Bag Toggle" it will enable you to move the bag as well (the controlls are differnt for the bag: U=Up, H=Right, L=Left and J=Down)')

    def Move_Step(self):
        """Changes how many tiles you move per step"""
        global evom_step
        step_move = Tksm.askinteger("Maze Config", "Input amount of steps you want to move with each input (high number inputs will cause errors)")
        if step_move == None:
            step_move = evom_step
            print(f"Invalid input keeping steps moved from input at {step_move}")
        else:
            print(f"Steps moved from input changed to {step_move}")
        evom_step = step_move


    def BagMoveSet(self):
        """Toggles if the bag can move or not"""
        global evom_step
        global bag_sttep
        global bagcanmove
        if bagcanmove == True:
            bagcanmove = False
            bag_sttep = 0 
            #bor_step = evom_step
        elif bagcanmove == False:
            bagcanmove = True
            bag_sttep = evom_step
            #bor_step = 0


    #Boris Movement System
    
    def UMove(self):
        """Moves Boris Up"""
        global evom_step
        self.move("up",evom_step)
       
        if AreButtons == True:
            """Changes the color of the Up button when Boris moves if the buttons are enabled."""
            random_number = random.randint(1118481,16777215)
            hex_number = str(hex(random_number))
            hex_number = '#'+ hex_number [2:]
            
            self.boU.configure(bg=f"{hex_number}")
    
    def DMove(self):
        """Moves Boris Down"""
        global evom_step
        self.move("down",evom_step)
        
        if AreButtons == True:
            """Changes the color of the Down button when Boris moves if the buttons are enabled."""
            random_number = random.randint(1118481,16777215)
            hex_number = str(hex(random_number))
            hex_number = '#'+ hex_number [2:]
           
            self.boD.configure(bg=f"{hex_number}")
    
    def LMove(self):
        """Moves Boris Left"""
        global evom_step
        self.move("left",evom_step)
        
        if AreButtons == True:
            """Changes the color of the Left button when Boris moves if the buttons are enabled."""
            random_number = random.randint(1118481,16777215)
            hex_number = str(hex(random_number))
            hex_number = '#'+ hex_number [2:]
            
            self.boL.configure(bg=f"{hex_number}")

    def RMove(self):
        """Moves Boris Right"""
        global evom_step
        self.move("right",evom_step)
        
        if AreButtons == True:
            """Changes the color of the Right button when Boris moves if the buttons are enabled."""
            random_number = random.randint(1118481,16777215)
            hex_number = str(hex(random_number))
            hex_number = '#'+ hex_number [2:]
            
            self.boR.configure(bg=f"{hex_number}")


    #Bag Movement System
    
    def UMoveB(self):
        """Moves the Bag (Goal) Up"""
        global bag_sttep
        self.moveBag("up",bag_sttep)
    
    def DMoveB(self):
        """Moves the Bag (Goal) Down"""
        global bag_sttep
        self.moveBag("down",bag_sttep)
    
    def LMoveB(self):
        """Moves the Bag (Goal) Left"""
        global bag_sttep
        self.moveBag("left",bag_sttep)
    
    def RMoveB(self):
        """Moves the Bag (Goal) Right"""
        global bag_sttep
        self.moveBag("right",bag_sttep)



    #Debug Commands
    def debug_print(self):
        """Prints all info of both Boris and the Bag (Goal)"""
        print("\nBoris Info:")
        Swim.Sprite.print(self.boris)
        print("Bag (or Goal) Info:")
        Swim.Sprite.print(self.bag)
    
    def debug_move(self):
        """Moves Boris to the coordinates given. If inputs invalid number defaults to 0"""
        Xo = Tksm.askinteger("Maze Debug Config", "Input the X coordinate to place the player (1-20)")
        if Xo == None:
            Xo = self.boris.col+1
        Yo = Tksm.askinteger("Maze Debug Config", "Now input the Y coordinate to place the player (1-20)")
        if Yo == None:
            Yo = self.boris.row+1
        Xo = Xo-1
        Yo = Yo-1
        self.boris.col = Xo
        self.boris.row = Yo
        self.draw(self.maze_canvas)

    def debug_funct(self):
        """Gives the ability to call any function in the game (Unless it isn't in the dictionary below)"""
        function_dict = {'debug_move':self.debug_move,'debug_print':self.debug_print,"WinPop":self.WinPop,"Restart":self.Restart,"HelpMenu":self.HelpMenu,"BagMoveSet":self.BagMoveSet,"bag_colosion":self.bag_colosion}
        z = Tksm.askstring("Maze Debug Config", "Please input name of function you want to call")
        if z == '':
            None
        else:
            if z in function_dict:
                function_dict[z]()
            else:
                print("\nInvalid Function\n")
    


root = Tk()
abc = GameGUI(root)
root.mainloop()
