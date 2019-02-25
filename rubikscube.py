import numpy
from random import randint

one = ([1, 1, 1], [1, 1, 1], [1, 1, 1])
two = ([2, 2, 2], [2, 2, 2], [2, 2, 2])
three = ([3, 3, 3], [3, 3, 3], [3, 3, 3])
four = ([4, 4, 4], [4, 4, 4], [4, 4, 4])
five = ([5, 5, 5], [5, 5, 5], [5, 5, 5])
six = ([6, 6, 6], [6, 6, 6], [6, 6, 6])

global face1
global face2
global face3
global face4
global face5
global face6
face1 = numpy.array(one)
face2 = numpy.array(two)
face3 = numpy.array(three)
face4 = numpy.array(four)
face5 = numpy.array(five)
face6 = numpy.array(six)

def printCube():
    top = "     [1 2 3][4 5 6][7 8 9][101112]"
    line1 = "1:   " + "[     ]" + str(face5[0]) + "[     ]" + "[     ]"
    line2 = "2:   " + "[     ]" + str(face5[1]) + "[     ]" + "[     ]"
    line3 = "3:   " + "[     ]" + str(face5[2]) + "[     ]" + "[     ]"
    line4 = "4:   " + str(face1[0]) + str(face2[0]) + str(face3[0]) + str(face4[0])
    line5 = "5:   " + str(face1[1]) + str(face2[1]) + str(face3[1]) + str(face4[1])
    line6 = "6:   " + str(face1[2]) + str(face2[2]) + str(face3[2]) + str(face4[2])
    line7 = "7:   " + "[     ]" + str(face6[0]) + "[     ]" + "[     ]"
    line8 = "8:   " + "[     ]" + str(face6[1]) + "[     ]" + "[     ]"
    line9 = "9:   " + "[     ]" + str(face6[2]) + "[     ]" + "[     ]"
    print (top)
    print ("")
    print (line1)
    print (line2)
    print (line3)
    print (line4)
    print (line5)
    print (line6)
    print (line7)
    print (line8)
    print (line9)

def shiftDown(col):
    global rowNumber, s1, s2, s3, s4, s5, s6
    if (col == 1):
        rowNumber = 0
    elif (col == 2):
        rowNumber = 1
    elif(col == 3):
        rowNumber=2
    elif(col ==4):
        rowNumber = 0
    elif(col ==5):
        rowNumber = 1
    elif(col == 6):
        rowNumber = 2
    elif(col == 7):
        shiftUp(3)
    elif(col == 8):
        shiftUp(2)
    elif(col == 9):
        shiftUp(1)
    elif(col == 10):
        shiftUp(6)
    elif(col == 11):
        shiftUp(5)
    else:
        shiftUp(4)

    if (col == 1 or col == 2 or col == 3):
        if (col == 1):
            s1 = [face1[0][0], face1[1][0], face1[2][0]]
            s3 = [face3[0][2], face3[1][2], face3[2][2]]
            s5 = [face5[0][0], face5[0][1], face5[0][2]]
            s6 = [face6[2][0], face6[2][1], face6[2][2]]
            face1[0][0] = s5[2]
            face1[1][0] = s5[1]
            face1[2][0] = s5[0]
            face6[2][0] = s1[0]
            face6[2][1] = s1[1]
            face6[2][2] = s1[2]
            face3[0][2] = s6[2]
            face3[1][2] = s6[1]
            face3[2][2] = s6[0]
            face5[0][0] = s3[0]
            face5[0][1] = s3[1]
            face5[0][2] = s3[2]
            rotateFaceRight(face4)
        elif (col == 2):
            s1 = [face1[0][1], face1[1][1], face1[2][1]]
            s3 = [face3[0][1], face3[1][1], face3[2][1]]
            s5 = [face5[1][0], face5[1][1], face5[1][2]]
            s6 = [face6[1][0], face6[1][1], face6[1][2]]
            face1[0][1] = s5[2]
            face1[1][1] = s5[1]
            face1[2][1] = s5[0]
            face6[1][0] = s1[0]
            face6[1][1] = s1[1]
            face6[1][2] = s1[2]
            face3[0][1] = s6[2]
            face3[1][1] = s6[1]
            face3[2][1] = s6[0]
            face5[1][0] = s3[0]
            face5[1][1] = s3[1]
            face5[1][2] = s3[2]
        else:
            s1 = [face1[0][2], face1[1][2], face1[2][2]]
            s3 = [face3[0][0], face3[1][0], face3[2][0]]
            s5 = [face5[2][0], face5[2][1], face5[2][2]]
            s6 = [face6[0][0], face6[0][1], face6[0][2]]
            face1[0][2] = s5[2]
            face1[1][2] = s5[1]
            face1[2][2] = s5[0]
            face6[0][0] = s1[0]
            face6[0][1] = s1[1]
            face6[0][2] = s1[2]
            face3[0][0] = s6[2]
            face3[1][0] = s6[1]
            face3[2][0] = s6[0]
            face5[2][0] = s3[0]
            face5[2][1] = s3[1]
            face5[2][2] = s3[2]
            rotateFaceLeft(face2)

    if(col == 4 or col == 5 or col == 6):
        if (col == 4):
            s4 = [face4[0][rowNumber + 2], face4[1][rowNumber + 2], face4[2][rowNumber + 2]]
            rotateFaceRight(face1)
        elif (col == 5):
            s4 = [face4[0][rowNumber], face4[1][rowNumber], face4[2][rowNumber]]
        else:
            s4 = [face4[0][rowNumber - 2], face4[1][rowNumber - 2], face4[2][rowNumber - 2]]
            rotateFaceLeft(face3)
        s5 = [face5[0][rowNumber], face5[1][rowNumber], face5[2][rowNumber]]
        s2 = [face2[0][rowNumber], face2[1][rowNumber], face2[2][rowNumber]]
        s6 = [face6[0][rowNumber], face6[1][rowNumber], face6[2][rowNumber]]
        face5[0][rowNumber] = s4[0]
        face5[1][rowNumber] = s4[1]
        face5[2][rowNumber] = s4[2]
        face2[0][rowNumber] = s5[0]
        face2[1][rowNumber] = s5[1]
        face2[2][rowNumber] = s5[2]
        face6[0][rowNumber] = s2[0]
        face6[1][rowNumber] = s2[1]
        face6[2][rowNumber] = s2[2]
        if(col == 4):
            face4[0][rowNumber + 2] = s6[0]
            face4[1][rowNumber + 2] = s6[1]
            face4[2][rowNumber + 2] = s6[2]
        elif(col == 5):
            face4[0][rowNumber] = s6[0]
            face4[1][rowNumber] = s6[1]
            face4[2][rowNumber] = s6[2]
        else:
            face4[0][rowNumber - 2] = s6[0]
            face4[1][rowNumber - 2] = s6[1]
            face4[2][rowNumber - 2] = s6[2]

def shiftUp(col):
    shiftDown(col)
    shiftDown(col)
    shiftDown(col)

def shiftRight(row):
    if (row == 1):
        shiftDown(9)
    elif (row == 2):
        shiftDown(8)
    elif (row == 3):
        shiftDown(7)
    elif(row == 4):
        rowNumber = 0
        rotateFaceLeft(face5)
    elif(row == 5):
        rowNumber = 1
    elif(row == 6):
        rowNumber = 2
        rotateFaceRight(face6)
    elif (row == 7):
        shiftDown(3)
    elif (row == 7):
        shiftDown(2)
    else:
        shiftDown(1)

    if(row == 4 or row == 5 or row == 6):
        s1 = [face1[rowNumber][0], face1[rowNumber][1], face1[rowNumber][2]]
        s2 = [face2[rowNumber][0], face2[rowNumber][1], face2[rowNumber][2]]
        s3 = [face3[rowNumber][0], face3[rowNumber][1], face3[rowNumber][2]]
        s4 = [face4[rowNumber][0], face4[rowNumber][1], face4[rowNumber][2]]
        face1[rowNumber][0] = s4[0]
        face1[rowNumber][1] = s4[1]
        face1[rowNumber][2] = s4[2]
        face2[rowNumber][0] = s1[0]
        face2[rowNumber][1] = s1[1]
        face2[rowNumber][2] = s1[2]
        face3[rowNumber][0] = s2[0]
        face3[rowNumber][1] = s2[1]
        face3[rowNumber][2] = s2[2]
        face4[rowNumber][0] = s3[0]
        face4[rowNumber][1] = s3[1]
        face4[rowNumber][2] = s3[2]

def shiftLeft(row):
    shiftRight(row)
    shiftRight(row)
    shiftRight(row)

def rotateFaceRight(face):
    r1 = [face[0][0], face[0][1], face[0][2]]
    r2 = [face[1][0], face[1][1], face[1][2]]
    r3 = [face[2][0], face[2][1], face[2][2]]

    #reassign the face values in the correct order
    face[0][0] = r3[0]
    face[0][1] = r2[0]
    face[0][2] = r1[0]
    face[1][0] = r3[1]
    face[1][1] = r2[1]
    face[1][2] = r1[1]
    face[2][0] = r3[2]
    face[2][1] = r2[2]
    face[2][2] = r1[2]

def rotateFaceLeft(face):
    rotateFaceRight(face)
    rotateFaceRight(face)
    rotateFaceRight(face)

def shuffle():
    for x in range(15):
        methodPick = randint(1,4)
        if(methodPick == 1 or methodPick == 2):
            cellMove = randint(1, 12)
            if(methodPick == 1):
                shiftDown(cellMove)
            else:
                shiftUp(cellMove)
        else:
            cellMove = randint(1, 9)
            if(methodPick == 3):
                shiftRight(cellMove)
            else:
                shiftLeft(cellMove)

def welcome():
    print ("Welcome to pyCube! This is an ascii Rubik's cube")
    instructions()

def instructions():
    print ("Type: ")
    print ("i for instructions")
    print ("u + the column number will move that column up")
    print ("d + the column number will move that column down")
    print ("l + the row number will move that row left")
    print ("r + the column number will move that row right")
    print ("s for shuffling the Rubik's cube")
    print ("q to quit the game")
    print ("")
    print ("")
    printCube()

def quit():
    print ("")
    print ("Thank you for playing!")

def run():
    global turns
    choice = input("Type the move you would like to make: ")
    choice = choice.strip().lower()
    if(choice == ""):
        turns -= 1
        print ("Invalid entry!")
        return True
    elif(choice[0] == "i"):
        turns -= 1
        instructions()
        return True
    elif(choice[0] == "q"):
        quit()
        return False
    elif(choice[0] == "d"):
        try:
            num = int(choice[1])
            shiftDown(num)
            printCube()
            return True
        except:
            turns -= 1
            print ("Invalid entry!")
            return True
    elif (choice[0] == "u"):
        try:
            num = int(choice[1])
            shiftUp(num)
            printCube()
            return True
        except:
            turns -= 1
            print ("Invalid entry!")
            return True
    elif (choice[0] == "r"):
        try:
            num = int(choice[1])
            shiftRight(num)
            printCube()
            return True
        except:
            turns -= 1
            print ("Invalid entry!")
            return True
    elif (choice[0] == "l"):
        try:
            num = int(choice[1])
            shiftLeft(num)
            printCube()
            return True
        except:
            turns -= 1
            print ("Invalid entry!")
            return True
    elif(choice[0] == "s"):
        turns -= 1
        shuffle()
        printCube()
        return True
    else:
        turns -= 1
        print ("Invalid entry!")
        return True

if __name__ == '__main__':
    welcome()
    turns = 0
    while(run()):
        turns += 1
        print ("")
        print ("Turn: " + str(turns))
