from numpyNotes import *
import numpy as np

def simplexSolver(matrix, basic):
    #basicVar = [basic[i].get() for i in range(len(basic))]
    print(matrix)
    columnLastIndex = len(matrix[0]) - 1
    rowLastIndex = len(matrix) - 1

    #print(basicVar)

    while True:

        #lastcolumn will =  a reference to matrix's last array
        lastColumn = matrix[rowLastIndex]

        objectiveRow = [matrix[i][columnLastIndex] for i in range(len(matrix))]
        zValue = objectiveRow.pop()

        biggestNegativeIndex = find_min_of_obj(objectiveRow)

        if biggestNegativeIndex is None:
            print("exiting...\n\n")
            print("Final matrix is: " + str(matrix))
            print("Final Solution: " + str(zValue))

            exit()
        else:
            print("in else")
            print("The Biggest Negative Index is: " + str(biggestNegativeIndex))

            pivot_ColumnIndex = biggestNegativeIndex
            pivot_RowIndex = minimum_Theta_ratios(matrix, pivot_ColumnIndex, lastColumn)

            print("The Pivot Index is: " + str(pivot_RowIndex))

            manipulatingRows(matrix, pivot_ColumnIndex, pivot_RowIndex)




    # TODO:CREATE A SIMPLEX SOLVER

def find_min_of_obj(objectiveRow):
    print("In find_min_of_obj")
    print(objectiveRow)

    minimum = None

    #Last entry is z value

    print("Objective Row: " + str(objectiveRow))

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
        try:
            value = lastColumn[i]/columnEntries[i]
            thetavals.append(value)
        except ZeroDivisionError:
            thetavals.append(0)

    print(thetavals)
    #Minimum works for all generator objects
    pivotRowIndex = thetavals.index(min(value for value in thetavals if value > 0))

    return pivotRowIndex


def manipulatingRows(matrix, pivot_ColumnIndex, pivot_RowIndex):
    print("Manipulating rows")
    print("Before transformation: " + str(matrix))

    pivotEntry = matrix[pivot_ColumnIndex][pivot_RowIndex]

    print("pivot Entry is:" + str(pivotEntry))

    #Part 1
    for column in range(len(matrix)):
        matrix[column][pivot_RowIndex] = (matrix[column][pivot_RowIndex] / pivotEntry)

    print("Transforming after part 1:" + str(matrix))

    #Part 2
    for row in range(len(matrix[0])):
        if row == pivot_RowIndex:
            continue
        else:
            pivotColumn_Entry = matrix[pivot_ColumnIndex][row]
            multiple = -1 * pivotColumn_Entry
            for column in range(len(matrix)):
                entry = matrix[column][row]
                matrix[column][row] = entry + multiple * matrix[column][pivot_RowIndex]


    print("Transforming after part 2" + str(matrix))
    return matrix

