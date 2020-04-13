from numpyNotes import *
import numpy as np

def simplexSolver(matrix, basic):
    basicVar = [basic[i].get() for i in range(len(basic))]
    print(matrix)
    columnLastIndex = len(matrix[0]) - 1
    rowLastIndex = len(matrix) - 1

    print(basicVar)

    objectiveRow = [matrix[i][columnLastIndex] for i in range(len(matrix))]
    lastColumn = matrix[rowLastIndex]

    while True:
        biggestNegativeIndex = find_min_of_obj(objectiveRow)

        if biggestNegativeIndex is None:
            print("exiting...")
            exit()
        else:
            print("in else")
            print("The Biggest Negative Index is: " + str(biggestNegativeIndex))
            pivotIndex = minimum_Theta_ratios(matrix, biggestNegativeIndex, lastColumn)
            print("The Pivot Index is: " + str(pivotIndex))

            exit()


    # TODO:CREATE A SIMPLEX SOLVER

def find_min_of_obj(objectiveRow):
    print("In find_min_of_obj")
    print(objectiveRow)

    minimum = None

    #Last entry is z value
    objectiveRow.pop()
    print("Objective Row after Pop: " + str(objectiveRow))

    for minimumIndex in range(len(objectiveRow)):
        value = objectiveRow[minimumIndex]
        try:
            if value < 0:
                if value < minimum:
                    minimum = value
        except:
            minimum = value
    try:
        return objectiveRow.index(minimum)
    except:
        return None


def minimum_Theta_ratios(matrix, columnIndex, lastColumn):
    print("in minimum Theta Ratios")

    columnEntries = matrix[columnIndex]
    thetavals = []
    print("lastcolumn is: " + str(lastColumn))

    for i in range(len(columnEntries)):
        thetavals.append(lastColumn[i]/columnEntries[i])

    print(thetavals)
    #Minimum works for all generator objects
    pivotIndex = thetavals.index(min(value for value in thetavals if value > 0))

    return pivotIndex


def 