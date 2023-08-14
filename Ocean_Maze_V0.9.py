"""
'Title: Ocean Maze'
Author: Bailey Reid
Date: 29/07/22
Version: 0.9
Purpose:
https://tkdocs.com/tutorial/index.html
"""

''''All *double hash*(color) *double hash* are for an extention I use that highlighs the code that is contained in (can't use the character thing or it breaks)'''
#Example ##red would make the text red
from tkinter import Tk, NW, Canvas, StringVar, Frame, Button, Label, PhotoImage, Menu, Text, messagebox, Toplevel  # import Tk (Tcl/Tk) Interface,
import tkinter.simpledialog as Tksm
import sys
import random
import sys
from time import sleep
from PIL import Image, ImageTk


import pathlib
sys.path.insert(0,"Maze_Generation_Modules")

import Swim
import Ocean
##



#Asks if the player wants buttons to be enabled

streamline = Ocean.streamline

if streamline == False:
    movesys = messagebox.askquestion(message='Do You Want To Be Able To Use Buttons?',icon='question', title='Maze Setup')
    if movesys == 'yes':
        AreButtons = True
    else:
        AreButtons = False
else:
    AreButtons = True

class GameGUI():
    """
    The GameGUI class contains a Frame so we can add buttons when it is initiated it receives a Graphical user interface
    tool kit
    tk as an argument.
    """

    DebugMode = True

    evom_step = 1
    boat_sttep = 0
    boatcanmove = False
    
    error_has = False
    HasWon = False

    cursoz = ["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek"]

    A = 0
    Ad = 0
    Au = 0
    Al = 0
    Ar = 0
    sp = 0

    sprit = 'norm'

    restarted = False

    def WinPop(shelf):
        """This is the win screen system so when you get to the goal at the end of the maze"""
        #Col = Left/Right
        #Row = Up/Down
        win = Toplevel()
        win.title('You Win!!!!')

        def rvw():
            """Function to allow the restart button on the win screen to work because I couldn't figure out how to run two command on a button without using a function"""
            shelf.Restart()
            win.destroy()

        message = "Congrats you've gotten the boat so you win!"
        lablab = Label(win, text=message)
        lablab.grid(column=2,row=0)

        bto = Button(win, text="Restart",command=rvw)
        bto.grid(column=1,row=1)

        btt = Button(win, text="Get this message outa my face",command=win.destroy)
        btt.grid(column=2,row=1)

        btth = Button(win, text="Exit",command=shelf.frame.master.destroy)
        btth.grid(column=3,row=1)

    def boat_colosion(shelf):
        """This is what happens when the boat hits the player instad of the player hitting the boat"""
        print('Exception in Boat callback\nTraceback (most recent call last):\n  File "Ocean_Maze_V0.8.py", line ∞, in <collision>\n    if Swim.Sprite.hit(shelf,shelf.boris,shelf.boat):\nUnexpectedError: "You are not supposed to hit the player with the boat"')

    ##orange Draw Map
    def draw(shelf, canvas):
        """
        the draw map method"""
        canvas.delete('all')
        for row in range(shelf.ocean.HEIGHT):
            for col in range(shelf.ocean.WIDTH):
                if "e" in shelf.ocean.get(row,col):
                    dub = shelf.ocean.get(row,col)
                    canvas.create_image((col * shelf.ocean.TILESIZEY)+2, (row * shelf.ocean.TILESIZEX)+2, image=shelf.emg_vault[dub], anchor=NW)
                #
                elif "w" in shelf.ocean.get(row,col):
                    dub = shelf.ocean.get(row,col)
                    canvas.create_image((col * shelf.ocean.TILESIZEY)+2, (row * shelf.ocean.TILESIZEX)+2, image=shelf.wmg_vault[dub], anchor=NW)

                else:
                    print("Idfk Man")
            canvas.create_image(shelf.boat.col*shelf.ocean.TILESIZEX+2,shelf.boat.row*shelf.ocean.TILESIZEY+2,image = shelf.BoatImg,anchor=NW)
            canvas.create_image(shelf.boris.col*shelf.ocean.TILESIZEX+2,shelf.boris.row*shelf.ocean.TILESIZEY+2,image = shelf.BorisImg,anchor=NW)
            canvas.create_image(shelf.boris.col*shelf.ocean.TILESIZEX+2,shelf.boris.row*shelf.ocean.TILESIZEY+2,image = shelf.BorisClImg,anchor=NW)
## ##pink
    def move(shelf,x,y):
        """Both the movement system and the win colision system for Boris"""
        
        shelf.boris.move(x,y,shelf.ocean)
        shelf.draw(shelf.maze_canvas)
        shelf.restarted = False
        if Swim.Sprite.hit(shelf,shelf.boris,shelf.boat):
            if shelf.HasWon == False:
                print("You Win!!!")
                shelf.WinPop()
                shelf.HasWon = True
        elif shelf.A >= shelf.sp-1:
            shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisLineFace.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
            shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisBlue.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
            shelf.draw(shelf.maze_canvas)
            if shelf.A >= shelf.sp+24:
                shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisAngrey.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
                shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisRed.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
                shelf.draw(shelf.maze_canvas)
                if shelf.A >= shelf.sp+59:
                    shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisSad.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
                    shelf.draw(shelf.maze_canvas)
                    shelf.almostdead
            
    def almostdead(shelf):
        if shelf.restarted == True:
            None
        else:
            if shelf.sprit == "alt":
                shelf.sprit = "norm"
                shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisRed.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
            else:
                shelf.sprit = "alt"
                shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisRedAlt.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
            shelf.draw(shelf.maze_canvas)
            shelf.Short.after(500,shelf.almostdead)

    
    def moveBoat(shelf,x,y):
        """Both the movement system and the colision system for the Boat (Goal)"""
        shelf.boat.move(x,y,shelf.ocean)
        shelf.draw(shelf.maze_canvas)
        if shelf.error_has == False:
            if Swim.Sprite.hit(shelf,shelf.boris,shelf.boat):
                shelf.boat_colosion()
                shelf.error_has = True
        else:
            None
##

    def __init__(shelf,master):
        
        
        def nothinghere(event):
            """Function that's used as a placeholder for when a function isn't yet created"""
            print(event)

    ##green   
        """the initiate method imports images"""
        shelf.frame = Frame(master)
        shelf.frame.pack()
        shelf.ocean = Ocean.Ocean()
        shelf.boris = Swim.Sprite("Boris",shelf.ocean.PY,shelf.ocean.PX)
        shelf.boat = Swim.Sprite("Boat",shelf.ocean.GY,shelf.ocean.GX)
        shelf.start=(shelf.ocean.PY,shelf.ocean.PX)
        shelf.finish=(shelf.ocean.GY,shelf.ocean.GX)
        print(f'\nMaze Height = {shelf.ocean.HEIGHT}\nMaze Width = {shelf.ocean.WIDTH}')
        shelf.path_short()
        # Set up images
        shelf.wmg_vault = {"w":ImageTk.PhotoImage(Image.open("./Wssets/W.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wa":ImageTk.PhotoImage(Image.open("./Wssets/A.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wb":ImageTk.PhotoImage(Image.open("./Wssets/B.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wc":ImageTk.PhotoImage(Image.open("./Wssets/C.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wd":ImageTk.PhotoImage(Image.open("./Wssets/D.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wg":ImageTk.PhotoImage(Image.open("./Wssets/G.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wi":ImageTk.PhotoImage(Image.open("./Wssets/I.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wj":ImageTk.PhotoImage(Image.open("./Wssets/J.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wl":ImageTk.PhotoImage(Image.open("./Wssets/L.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wn":ImageTk.PhotoImage(Image.open("./Wssets/N.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wp":ImageTk.PhotoImage(Image.open("./Wssets/P.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wq":ImageTk.PhotoImage(Image.open("./Wssets/Q.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wr":ImageTk.PhotoImage(Image.open("./Wssets/R.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ws":ImageTk.PhotoImage(Image.open("./Wssets/S.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wt":ImageTk.PhotoImage(Image.open("./Wssets/T.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wu":ImageTk.PhotoImage(Image.open("./Wssets/U.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wx":ImageTk.PhotoImage(Image.open("./Wssets/X.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))}
        shelf.emg_vault = {"e":ImageTk.PhotoImage(Image.open("./Essets/E.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ea":ImageTk.PhotoImage(Image.open("./Essets/E.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eb":ImageTk.PhotoImage(Image.open("./Essets/EB.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ec":ImageTk.PhotoImage(Image.open("./Essets/EC.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ed":ImageTk.PhotoImage(Image.open("./Essets/ED.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eg":ImageTk.PhotoImage(Image.open("./Essets/EG.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ei":ImageTk.PhotoImage(Image.open("./Essets/EI.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ej":ImageTk.PhotoImage(Image.open("./Essets/EJ.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"el":ImageTk.PhotoImage(Image.open("./Essets/EL.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"en":ImageTk.PhotoImage(Image.open("./Essets/EN.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ep":ImageTk.PhotoImage(Image.open("./Essets/EP.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eq":ImageTk.PhotoImage(Image.open("./Essets/EQ.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"er":ImageTk.PhotoImage(Image.open("./Essets/ER.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"es":ImageTk.PhotoImage(Image.open("./Essets/ES.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"et":ImageTk.PhotoImage(Image.open("./Essets/ET.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eu":ImageTk.PhotoImage(Image.open("./Essets/EU.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ex":ImageTk.PhotoImage(Image.open("./Essets/EX.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))}
        shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisHappy.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisGreen.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.BoatImg = ImageTk.PhotoImage(Image.open("./Assets/Bag_32x32.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        # set up canvas for map
        shelf.maze_canvas = Canvas(shelf.frame, bg='#ffffff', height=shelf.ocean.HEIGHT * shelf.ocean.TILESIZEY, width=shelf.ocean.WIDTH * shelf.ocean.TILESIZEX)
        shelf.maze_canvas.grid(row=1, column=0, columnspan=3, rowspan=3)
        shelf.draw(shelf.maze_canvas)

        # set title of window
        shelf.frame.master.wm_title('Lmao Maze')
        shelf.frame.master.wm_iconbitmap(pathlib.Path("./Assets/Boris.ico"))
    ##



        
        ##blue Menu Bars
        
        shelf.menubar = Menu(shelf.frame)
        shelf.frame.master.config(menu=shelf.menubar)
        
        shelf.filemenu = Menu(shelf.menubar,tearoff=0)
        shelf.filemenu.add_command(label="Restart",command=lambda: shelf.Restart())
        shelf.filemenu.add_separator()
        shelf.filemenu.add_command(label="Exit",command=shelf.frame.master.destroy)

        shelf.menubar.add_cascade(label="File",menu=shelf.filemenu)
    
        
        shelf.helpmenu = Menu(shelf.menubar,tearoff=0)
        
        shelf.helpmenu.add_command(label="Help",command=lambda :shelf.menus("help"))
        shelf.helpmenu.add_separator()
        shelf.helpmenu.add_command(label="About",command=lambda :shelf.menus("about"))
        
        shelf.menubar.add_cascade(label="About",menu=shelf.helpmenu)

        
        shelf.configmenu = Menu(shelf.menubar,tearoff=0)

        shelf.configmenu.add_command(label="Movable Boat Toggle",command=shelf.BoatMoveSet)
        shelf.configmenu.add_separator()
        shelf.configmenu.add_command(label="Animate Asset",command=shelf.almostdead)


        shelf.menubar.add_cascade(label="Config",menu=shelf.configmenu)

        if shelf.DebugMode == True:
            #All the debug options for when debug move is turned on
            shelf.debugmenu = Menu(shelf.menubar,tearoff=0)
            shelf.debugmenu.add_command(label="Print Info",command=shelf.debug_print)
            shelf.debugmenu.add_separator()
            shelf.debugmenu.add_command(label="Select Move Character",command=shelf.debug_move)
            shelf.debugmenu.add_separator()
            shelf.debugmenu.add_command(label="Move Per Step",command=shelf.Move_Step)
            shelf.debugmenu.add_separator()
            shelf.debugmenu.add_command(label="Update Assets",command=shelf.debug_upasset)
            shelf.debugmenu.add_separator()

            
            shelf.debugmenu.add_command(label="Call Function",command=shelf.debug_funct)

            shelf.menubar.add_cascade(label="Debug",menu=shelf.debugmenu)



        shelf.frame.master['menu'] = shelf.menubar ##

        
        #Buttons
        if AreButtons == True:
            
            """Method of placing buttons on the window if option "yes" is picked"""
            print('\nOption Yes Was Picked For Buttons, Placing Buttons\n')

            shelf.boU = Button(shelf.frame, text=f"Up: {shelf.Au}", cursor=random.choice(shelf.cursoz), command=shelf.UMove)
            shelf.boU.grid(row=20, column=1)

            
            shelf.boL = Button(shelf.frame, text=f"Left: {shelf.Al}", cursor=random.choice(shelf.cursoz), command=shelf.LMove)
            shelf.boL.grid(row=21, column=0)
        

            shelf.boD = Button(shelf.frame, text=f"Down: {shelf.Ad}", cursor=random.choice(shelf.cursoz), command=shelf.DMove)
            shelf.boD.grid(row=22, column=1)

            shelf.boR = Button(shelf.frame, text=f"Right: {shelf.Ar}", cursor=random.choice(shelf.cursoz), command=shelf.RMove)
            shelf.boR.grid(row=21, column=2)

            shelf.Short = Button(shelf.frame, text=f"Total: {shelf.A}", cursor=random.choice(shelf.cursoz), command=shelf.almostdead)
            shelf.Short.grid(row=21, column=1)

            shelf.sp_label = Label(shelf.frame, text=f"Shortest Path: {shelf.sp}")
            shelf.sp_label.grid(row=0, column=1)
        else:
            shelf.toalz=Label(shelf.frame, text="Total: 0")
            shelf.toalz.grid(row=0, column=0)

            shelf.sp_label = Label(shelf.frame, text=f"Shortest Path: {shelf.sp}")
            shelf.sp_label.grid(row=0, column=2)


        
        
        #Keybinds
        #fa6665 
        
        #Binds keybinds to the movement system to be able to move with WASD
        master.bind('w', lambda event: shelf.UMove())
        master.bind('s', lambda event: shelf.DMove())
        master.bind('a', lambda event: shelf.LMove())
        master.bind('d', lambda event: shelf.RMove())
        master.bind('<Escape>', lambda event: shelf.frame.master.destroy())
        
        

        #Boat Keybinds
        
        #The same as the other keybinds but allows the Boat (Goal) to be moved with UJHK instead
        master.bind('u', lambda event: shelf.UMoveB())
        master.bind('j', lambda event: shelf.DMoveB())
        master.bind('h', lambda event: shelf.LMoveB())
        master.bind('k', lambda event: shelf.RMoveB())


    #Menu Bar Functions
    
    def Restart(shelf):
        """Module for restarting the game once the player has either won or decided to restart via the file menu"""
        
        shelf.boris.restartS(shelf.ocean.PY,shelf.ocean.PX)
        shelf.boat.restartS(shelf.ocean.GY,shelf.ocean.GX)
        shelf.restarted = True
        shelf.HasWon = False
        
        shelf.A = 0
        shelf.Ad = 0
        shelf.Au = 0
        shelf.Al = 0
        shelf.Ar = 0

        shelf.boU.configure(text=f"Up: {shelf.Au}",bg="#ffffff")
        shelf.boD.configure(text=f"Down: {shelf.Ad}",bg="#ffffff")
        shelf.boL.configure(text=f"Left: {shelf.Al}",bg="#ffffff")
        shelf.boR.configure(text=f"Right: {shelf.Ar}",bg="#ffffff")
        shelf.Short.configure(text=f"Total: {shelf.A}",bg="#ffffff")
        shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisHappy.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisGreen.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.draw(shelf.maze_canvas)


    def menus(shelf,opt):
        """Module for the two menu bars that display infomation"""
        if opt == "about":
            """Module for displaying infomation about the maze game thing"""
            messagebox.showinfo('About', "Title: Ocean Maze\nAuthor: Bailey Reid\nVersion: 0.9\nAn attempt to create a somewhat interesting maze")
        elif opt == "help":
            """Explains how to play the game and what your objective is"""
            if AreButtons == True:
                messagebox.showinfo('Help', 'Your main goal is to reach the boat at the other end of the maze, touching it will make you win.\n\nYou have two movement options WASD and the buttons at the bottem of your screen.\n\nWASD are four keys on the keyboard that coraspond to the four directions you can move Up(W), Down(S), Left(L) and Right(D).\n\nThe Buttons are arrange in a way to make it easy to tell which direction they coraspond to, for exaample the button on top moves the character up.\n\nIf you go to config and turn on the "Movable Boat Toggle" it will enable you to move the boat as well (the controlls are differnt for the boat: U=Up, H=Right, L=Left and J=Down)')
            else:
                messagebox.showinfo('Help', 'Your main goal is to reach the boat at the other end of the maze, touching it will make you win.\n\nThe way to controll the character on screen is using WASD\nWASD are four keys on the keyboard that coraspond to the four directions you can move Up(W), Down(S), Left(L) and Right(D).\n\nIf you go to config and turn on the "Movable Boat Toggle" it will enable you to move the boat as well (the controlls are differnt for the boat: U=Up, H=Right, L=Left and J=Down)')
        
        
    def Move_Step(shelf):
        """Changes how many tiles you move per step"""
        
        step_move = Tksm.askinteger("Maze Config", "Input amount of steps you want to move with each input (high number inputs will cause errors)")
        if step_move == None:
            step_move = shelf.evom_step
            print(f"Invalid input keeping steps moved from input at {step_move}")
        else:
            print(f"Steps moved from input changed to {step_move}")
        shelf.evom_step = step_move


    def BoatMoveSet(shelf):
        """Toggles if the boat can move or not"""
        
        
        if shelf.boatcanmove == True:
            shelf.boatcanmove = False
            shelf.boat_sttep = 0 
            #bor_step = evom_step
        elif shelf.boatcanmove == False:
            shelf.boatcanmove = True
            shelf.boat_sttep = shelf.evom_step
            #bor_step = 0


    ##red Boris Movement System
    def UMove(shelf,distance=evom_step):
        """Moves Boris Up"""
        if "e" in shelf.ocean.get(shelf.boris.row-distance,shelf.boris.col):
            shelf.move("up",shelf.evom_step)
            shelf.Au+=1
            shelf.A+=1
            if AreButtons == True:
                """Changes the color of the Up button when Boris moves if the buttons are enabled."""
                random_number = random.randint(1118481,16777215)
                hex_number = str(hex(random_number))
                hex_number = '#'+ hex_number [2:]

                shelf.boU.configure(text=f"Up: {shelf.Au}", bg=f"{hex_number}", cursor=random.choice(shelf.cursoz))
                shelf.Short.configure(text=f"Total: {shelf.A}")
            else:
                shelf.toalz.config(text=f"Total Moved: {shelf.A}")
    
    def DMove(shelf,distance=evom_step):
        """Moves Boris Down"""
        if "e" in shelf.ocean.get(shelf.boris.row+distance,shelf.boris.col):
            shelf.move("down",shelf.evom_step)
            shelf.Ad+=1
            shelf.A+=1
            if AreButtons == True:
                """Changes the color of the Down button when Boris moves if the buttons are enabled."""
                random_number = random.randint(1118481,16777215)
                hex_number = str(hex(random_number))
                hex_number = '#'+ hex_number [2:]

                shelf.boD.configure(text=f"Down: {shelf.Ad}", bg=f"{hex_number}", cursor=random.choice(shelf.cursoz))
                shelf.Short.configure(text=f"Total: {shelf.A}")
            else:
                shelf.toalz.config(text=f"Total Moved: {shelf.A}")

    def LMove(shelf,distance=evom_step):
        """Moves Boris Left"""
        if "e" in shelf.ocean.get(shelf.boris.row,shelf.boris.col-distance):
            shelf.move("left",shelf.evom_step)
            shelf.Al+=1
            shelf.A+=1
            if AreButtons == True:
                """Changes the color of the Left button when Boris moves if the buttons are enabled."""
                random_number = random.randint(1118481,16777215)
                hex_number = str(hex(random_number))
                hex_number = '#'+ hex_number [2:]

                shelf.boL.configure(text=f"Left: {shelf.Al}", bg=f"{hex_number}", cursor=random.choice(shelf.cursoz))
                shelf.Short.configure(text=f"Total: {shelf.A}")
            else:
                shelf.toalz.config(text=f"Total Moved: {shelf.A}")

    def RMove(shelf,distance=evom_step):
        """Moves Boris Right"""
        if "e" in shelf.ocean.get(shelf.boris.row,shelf.boris.col+distance):
            shelf.move("right",shelf.evom_step)
            shelf.Ar+=1
            shelf.A+=1
            if AreButtons == True:
                """Changes the color of the Right button when Boris moves if the buttons are enabled."""
                random_number = random.randint(1118481,16777215)
                hex_number = str(hex(random_number))
                hex_number = '#'+ hex_number [2:]

                shelf.boR.configure(text=f"Right: {shelf.Ar}", bg=f"{hex_number}", cursor=random.choice(shelf.cursoz))
                shelf.Short.configure(text=f"Total: {shelf.A}") 
            else:
                shelf.toalz.config(text=f"Total Moved: {shelf.A}")

##

    #Boat Movement System
    
    def UMoveB(shelf):
        """Moves the Boat (Goal) Up"""
        
        shelf.moveBoat("up",shelf.boat_sttep)
    
    def DMoveB(shelf):
        """Moves the Boat (Goal) Down"""
        
        shelf.moveBoat("down",shelf.boat_sttep)
    
    def LMoveB(shelf):
        """Moves the Boat (Goal) Left"""
        
        shelf.moveBoat("left",shelf.boat_sttep)
    
    def RMoveB(shelf):
        """Moves the Boat (Goal) Right"""
        
        shelf.moveBoat("right",shelf.boat_sttep)


    def path_short(shelf):
        #for y in range(shelf.ocean.HEIGHT):
        #    for x in range(shelf.ocean.WIDTH):
        shelf.sp=shelf.ocean.shortest(shelf.start,shelf.finish)

    def openmaze(shelf):
        shelf.ocean.loadm()
        shelf.Picker.restartS(shelf.ocean.PY,shelf.ocean.PX)
        shelf.Stoot.restartS(shelf.ocean.PY,shelf.ocean.PX)
        shelf.End.restartS(shelf.ocean.GY,shelf.ocean.GX)
        shelf.canvas_draw()

    
    def switchcl(shelf):
        shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisShocked.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.BorisClImg = ImageTk.PhotoImage(Image.open("./Bssets/BorisBlue.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.draw(shelf.maze_canvas)

    ##magenta Debug Commands
    def debug_print(shelf):
        """Prints all info of both Boris and the Boat (Goal)"""
        print("\nBoris Info:")
        Swim.Sprite.print(shelf.boris)
        print("Boat (or Goal) Info:")
        Swim.Sprite.print(shelf.boat)
    
    def debug_move(shelf):
        """Moves Boris to the coordinates given. If inputs invalid number defaults to 0"""
        Xo = Tksm.askinteger("Maze Debug Config", "Input the X coordinate to place the player (1-20)")
        if Xo == None:
            Xo = shelf.boris.col+1
        Yo = Tksm.askinteger("Maze Debug Config", "Now input the Y coordinate to place the player (1-20)")
        if Yo == None:
            Yo = shelf.boris.row+1
        Xo = Xo-1
        Yo = Yo-1
        shelf.boris.col = Xo
        shelf.boris.row = Yo
        shelf.draw(shelf.maze_canvas)
    
    def debug_upasset(shelf):
        shelf.wmg_vault = {"w":ImageTk.PhotoImage(Image.open("./Wssets/W.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wa":ImageTk.PhotoImage(Image.open("./Wssets/A.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wb":ImageTk.PhotoImage(Image.open("./Wssets/B.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wc":ImageTk.PhotoImage(Image.open("./Wssets/C.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wd":ImageTk.PhotoImage(Image.open("./Wssets/D.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wg":ImageTk.PhotoImage(Image.open("./Wssets/G.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wi":ImageTk.PhotoImage(Image.open("./Wssets/I.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wj":ImageTk.PhotoImage(Image.open("./Wssets/J.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wl":ImageTk.PhotoImage(Image.open("./Wssets/L.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wn":ImageTk.PhotoImage(Image.open("./Wssets/N.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wp":ImageTk.PhotoImage(Image.open("./Wssets/P.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wq":ImageTk.PhotoImage(Image.open("./Wssets/Q.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wr":ImageTk.PhotoImage(Image.open("./Wssets/R.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ws":ImageTk.PhotoImage(Image.open("./Wssets/S.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wt":ImageTk.PhotoImage(Image.open("./Wssets/T.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wu":ImageTk.PhotoImage(Image.open("./Wssets/U.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"wx":ImageTk.PhotoImage(Image.open("./Wssets/X.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))}
        shelf.emg_vault = {"e":ImageTk.PhotoImage(Image.open("./Essets/E.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ea":ImageTk.PhotoImage(Image.open("./Essets/E.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eb":ImageTk.PhotoImage(Image.open("./Essets/EB.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ec":ImageTk.PhotoImage(Image.open("./Essets/EC.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ed":ImageTk.PhotoImage(Image.open("./Essets/ED.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eg":ImageTk.PhotoImage(Image.open("./Essets/EG.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ei":ImageTk.PhotoImage(Image.open("./Essets/EI.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ej":ImageTk.PhotoImage(Image.open("./Essets/EJ.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"el":ImageTk.PhotoImage(Image.open("./Essets/EL.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"en":ImageTk.PhotoImage(Image.open("./Essets/EN.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ep":ImageTk.PhotoImage(Image.open("./Essets/EP.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eq":ImageTk.PhotoImage(Image.open("./Essets/EQ.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"er":ImageTk.PhotoImage(Image.open("./Essets/ER.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"es":ImageTk.PhotoImage(Image.open("./Essets/ES.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"et":ImageTk.PhotoImage(Image.open("./Essets/ET.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"eu":ImageTk.PhotoImage(Image.open("./Essets/EU.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX))),"ex":ImageTk.PhotoImage(Image.open("./Essets/EX.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))}
        shelf.BorisImg = ImageTk.PhotoImage(Image.open("./Assets/BorisRed.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.BoatImg = ImageTk.PhotoImage(Image.open("./Assets/Bag_32x32.png").resize((shelf.ocean.TILESIZEY,shelf.ocean.TILESIZEX)))
        shelf.draw(shelf.maze_canvas)

    def debug_funct(shelf):
        """Gives the ability to call any function in the game (Unless it isn't in the dictionary below)"""
        function_dict = {'debug_move':shelf.debug_move,'debug_print':shelf.debug_print,"WinPop":shelf.WinPop,"Restart":shelf.Restart,"BoatMoveSet":shelf.BoatMoveSet,"boat_colosion":shelf.boat_colosion,"debug_upasset":shelf.debug_upasset,"switchcl":shelf.switchcl}
        z = Tksm.askstring("Maze Debug Config", "Please input name of function you want to call")
        if z == '':
            None
        else:
            if z in function_dict:
                function_dict[z]()
            else:
                print("\nInvalid Function\n")
    
## 

root = Tk()
abc = GameGUI(root)
root.mainloop()

