
'''
INPUT FIELDS - CODECAMP

from tkinter import *

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


root = Tk()

e = Entry(root)
e.pack()
e.insert(0,"Enter Your Name")

myButton = Button(root, text = "Enter your Name", command=myClick)
myButton.pack()


root.mainloop()

BUCKY TUTORIAL - 1

root = Tk() #Tk() is a constructor for a window; default constructor is blank initialized to obj root
theLabel = Label(root, text="Sameet's first GUI")
theLabel.pack() #used to display paremeters initialized in label e.g. txt in the window created when calling Tk()
root.mainloop() #infinite loop until exit out the program




BUCKY TUTORIAL - 2

root = Tk()

topFrame = Frame(root)  #A FRAME IS JUST A BLANK EMPTY CONTAINER
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text="Button 1", fg = "red") #fg is color; opt.
button2 = Button(topFrame, text="Button 2", fg = "blue") #fg is color; opt.
button3 = Button(topFrame, text="Button 3", fg = "green") #fg is color; opt.
button4 = Button(bottomFrame, text="Button 4", fg = "purple") #fg is color; opt.
button5 = Button(bottomFrame, text = "Button 5", fg = "pink")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = LEFT)
button5.pack(side = LEFT)
``

root.mainloop()

Notes on pack:

!!! ANYTIME WE WANT TO DISPLAY AN OBJ. ON WINDOW; WE MUST .PACK() IT!!!"

pack() automatically puts each obj. on top of each other; to pack in other loc. (other than top or bottom RELATIVE to other obj.) pass in side = ... as parameter where ... can be LEFT, RIGHT, etc




BUCKY TUTORIAL - 3

root = Tk()

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()
two = Label (root, text = "Two", bg = "green", fg = "black")
two.pack(fill = BOTH, expand = TRUE) #fill the window in the x direction
three = Label(root, text = "Three", bg = "black", fg ="white")
three.pack(fill = BOTH, expand = TRUE)


root.mainloop()



Bucky Tutorial 4 & 5

#USING GRID (AN ALTERNATIVE WAY TO PACKING IN CREATING A LAYOUT 

root = Tk()

label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root) # A blank field where user can type something in
entry_2 = Entry(root)


label_1.grid(row=0, sticky = E) #sticky --> align with a direction  ~ N, S, E, W ~ in its cell
label_2.grid(row=1)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton (root, text = "Keep me logged in") #gives you a check box
c.grid(columnspan = 2)


root.mainloop()


BUCKY TUTORIAL - 6

BINDING FXNS TO LAYOUTS

#TECHNIQUE 1

root = Tk()

def printName():
    print("Hello World!")

button_1 = Button(root, text = "Print my name", command= printName) #will execute the function that command is associated w/
button_1.pack()

root.mainloop()


#TECHNIQUE 2

root = Tk()

def printName(event): #Event: something that occurs on a computer
    print ("Hello World!")

button_1 = Button(root, text = "Print my name")
button_1.bind("<Button-1>", printName) #.bind() fxn takes two parameters: WHAT EVENT TO OCCUR, WHAT COMMAND SHOULD HAPPEN WHEN EVENT OCCURS
button_1.pack()

root.mainloop()

BUCKY TUTORIAL - 8

    - BINDING MULTIPLE EVENTS TO A SINGLE OBJ

root = Tk()

def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")


def rightClick(event):
    print("right")

frame = Frame(root, width=300, height = 250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()


BUCKY TUTORIAL - 8

class Buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit) #frame.quit() breaks the main loop (essentially closes program)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")


root = Tk()

b = Buttons(root)

root.mainloop()



BUCKY TUTORIAL 9 - 12

- MENUS


def doNothing():
    print("ok I won't...")

root = Tk()

menu = Menu(root)
#menu.add_command(label="Hello!", command=doNothing)  WHY DOESN'T THE FOLLOWING WORK?

root.config(menu=menu) #.config(menu=<menu_name>) configures all attributes of that menu to a default


subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu=editMenu)
editMenu.add_command(label = "Redo", command=doNothing)

viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Zoom in", command=doNothing)
viewMenu.add_command(label="Zoom out", command=doNothing)

#**** CREATING TOOLBAR

toolbar = Frame(root, bg="blue")
insertB = Button(toolbar, text="Insert Image", command=doNothing)
insertB.pack(side=LEFT, padx=2, pady=2) #padding: extra space for button
printB = Button(toolbar, text="Print", command=doNothing)
printB.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#*** STATUS BAR

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN,  anchor=W) #bd stands for border
status.pack(side=BOTTOM, fill=X)

root.mainloop()


BUCKY TUTORIAL - 13

**MAKE SURE TO : import tkinster.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'First GUI')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like me?')

if answer == 'yes':
    print('Super Duper')
elif answer == 'no':
    print ('Allah hu Akbar')

root.mainloop()



BUCKY TUTORIAL - 13

- SHAPES 

root = Tk()

canvas = Canvas(root, width=200, height=100, bd=1, relief = SUNKEN)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle (25, 25, 130, 60, fill="Green")


root.mainloop()

'''
