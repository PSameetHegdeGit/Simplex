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

            pivotColumnIndex = biggestNegativeIndex
            pivotRowIndex = minimum_Theta_ratios(matrix, pivotColumnIndex, lastColumn)

            print("The Pivot Index is: " + str(pivotRowIndex))

            matrix = manipulatingRows(matrix, pivotRowIndex, pivotColumnIndex)

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
    pivotRowIndex = thetavals.index(min(value for value in thetavals if value > 0))

    return pivotRowIndex


def manipulatingRows(matrix, pivot_RowIndex, pivot_ColumnIndex):
    print("Manipulating rows")
    pivotEntry = matrix[pivot_RowIndex][pivot_ColumnIndex]

    #Part 1
    for i in range(len(matrix)):
        matrix[pivot_RowIndex][i] = matrix[pivot_RowIndex][i] / pivotEntry

    print(matrix)

    #Part 2
    for rowIndex in range(len(matrix[0])):
        if rowIndex == pivot_RowIndex:
            continue
        else:
            pivotColumn_Entry = matrix[rowIndex][pivot_ColumnIndex]
            multiple = -(pivotColumn_Entry/pivotEntry)
            for columnIndex in range(len(matrix)):
                matrix[rowIndex][i] = matrix[rowIndex][i] + multiple*matrix[rowIndex][columnIndex]

    print(matrix)
    return matrix

