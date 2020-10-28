from log import log
Log = log("log.txt")

# -*- coding: utf-8 -*-

board = [None for x in range(9)]

def empty(place):
    if board[place]:
        return False
    else:
        return True

def drawBoard():
    p = 0
    for i in range(3):
        line = ""
        for j in range(3):
            p += 1
            if board[p-1]:
                line += "| " + str(board[p-1]) + " |"
            else:
                line += "| " + str(p) + " |"
        print(line)
        print("="*15)

def inputPlace():
    #for i in range(9):
        place = None
        drawBoard()
        place = input("выберите место для 0 или X: ")
        if place in "123456789":
            place = int(place)
            if empty(place):
                board[place] = "X"
            else:
                print("=" * 31 + "\nместо " + str (place+1) + " занято! выберите другое")

def result():
    pass

#while not result():
#drawBoard()
inputPlace()
inputPlace()
inputPlace()
inputPlace()
inputPlace()
Log.end()