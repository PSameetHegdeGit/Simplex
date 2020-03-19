from numpyNotes import *

def simplexSolver(matrix, basic):
    basicVar = [basic[i].get() for i in range(len(basic))]
    print(matrix)
    print(basicVar)

    # TODO:CREATE A SIMPLEX SOLVER
