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

def inputPlace(z):
        place = None
        place = input("выберите место для " + z + ": ")
        if place.isdigit():
            place = int(place)-1
            if (place in range(9)) and (empty(place)):
                board[place] = z
                return True
            else:
                print("=" * 31 + "\nместо " + str (place+1) + " занято! выберите другое")
                return False
        else:
            print("недопустиное значение!")
            return False

def result(step):
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in victory:
        if (board[x[0]] == board[x[1]] == board[x[2]]) and (board[x[0]] != None):
            print (board[x[0]], "победил!")
            return True
        else:
            if step == 9:
                print ("ничья!")
                return True
    return False

step = 0
while not result(step):
    drawBoard()
    if step % 2 == 0:
        if inputPlace("X"): step += 1
    else:
        if inputPlace("O"): step += 1