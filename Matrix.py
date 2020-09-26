from tkinter import *
from Simplex import *
#Request Matrix size

def matrixCreator():

    x = int(entry1.get())
    y = int(entry2.get())

    #GET MATRIX ENTRY AND BASIC VARIABLE WINDOW
    matrixWindow = Tk()
    matrixWindow.title("Enter matrix below:")

    #Get Simplex Matrix
    matrix =[]
    for m in range(x):
        matrixhold = []
        for n in range(y):
            cell = Entry(matrixWindow, width=5, borderwidth=1)
            matrixhold.append(cell)
            cell.grid(row=m, column=n)
        matrix.append(matrixhold)

    Button(matrixWindow, text="Enter", padx=10, pady=5, command=lambda: matrixRetrieve(matrix, x, y, matrixWindow)).grid(row=x+1,columnspan=y)
    matrixWindow.mainloop()

def matrixRetrieve(matrix, x, y, window):
    matrixContent = [[int(matrix[i][j].get()) for i in range(x)] for j in range(y)]
    Label(window, text="Enter basic columns: ").grid(row=x+2,column=0)

    #Get Basic Variables
    basic = []
    for m in range(y):
        cell = Entry(window, width=5, borderwidth=1)
        basic.append(cell)
        cell.grid(row=x+2, column=m+1)

    Button(window, text="Enter Basic Variables", command=lambda: simplexSolver(matrixContent)).grid(row=x+2, column=y+1)



#SEEK MATRIX DIMENSION WINDOW
if __name__ == "__main__":
    root = Tk()
    root.title("Matrix")

    mylabel = Label(root, text = "Enter Matrix Dimensions Below:")
    mylabel.pack()

    entry1 = Entry(root, width=15, borderwidth=3)
    entry1.pack(side=LEFT)

    label2 = Label(root, text="X")
    label2.pack(side=LEFT)

    entry2 = Entry(root, width=15, borderwidth=3)
    entry2.pack(side=LEFT)

    dimButton = Button(root, text="Enter", padx = 10, pady = 5, command = matrixCreator)
    dimButton.pack(side=LEFT)

    root.mainloop()