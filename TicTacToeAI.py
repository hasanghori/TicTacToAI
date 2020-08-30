def checkWin (gameBoard,row, column):
    win = True #checks horizontal three in a row
    for x in range (0,3):
        if gameBoard[x][column] != gameBoard[row][column]:
            win = False
    if win == False: #checks vertical three in a row
        win = True
        for y in range(0,3):
            if gameBoard[row][y] != gameBoard[row][column]:
                win = False  
    if win == False: #checks diagonal three in a row
        if gameBoard[0][0] == gameBoard[row][column]:
            win = True
            for z in range (0,3):
                if gameBoard[z][z] != gameBoard[row][column]:
                    win = False                 
        if gameBoard[2][0] == gameBoard[row][column] and win == False:
            win = True
            for z in range (0,3):
                if gameBoard[2 - z][0 + z] != gameBoard[row][column]:
                    win = False
    return win            
def checkDraw (gameBoard, win):
    continueGame = True
    if win == False:
        for x in range(0, 3):
            for y in range(0, 3):
                if gameBoard[x][y] == int(0):
                    continueGame = False
    return continueGame
def miniMax (gameBoard):
    while win == False and draw == False:
    #Player 1 Method
        player1 = int(1)
        print("Player 1 select your move")
        rowColArrayOne = AIplayer(gameBoard)
    
    #column = int(input("select column"))-1
    #row = int(input("select row"))-1
    
        column = int(rowColArrayOne["col"])
        row = int(rowColArrayOne["row"])
        gameBoard[row][column] = int(1)
    
        for x in range(0,3):
            print(gameBoard[x])
        win = checkWin(gameBoard, row, column)
        draw = checkDraw(gameBoard, win)
        if win or draw:
            break
    #Player 2 Method
        player2 = int(2)
        print("Player 2 select your move")
        rowColArray = AIplayer(gameBoard)
        column = int(rowColArray["col"])
        row = int(rowColArray["row"])
        gameBoard[row][column] = int(2)
        for x in range(0,3):
            print(gameBoard[x])
        win = checkWin(gameBoard, row, column)
        draw = checkDraw(gameBoard, win)
    
def AIplayer (gameBoard):
    #gameBoardCopy = [[int(0) for x in range(3)] for y in range(3)]
    gameBoardCopy = Move(gameBoard)
    highestScore = int(0)
    rowColArray = {"row": int(0),"col": int(0)}
    for x in range(0,3):
        for y in range(0,3):
            if gameBoardCopy[x][y] > highestScore and gameBoard[x][y] == int(0):
                rowColArray["row"] = int(x)
                rowColArray["col"] = int(y)
                highestScore = gameBoardCopy[x][y]
    return rowColArray
def Move (gameBoard):
    #this will call the score method
    gameBoardCopy = [[int(0) for x in range(3)] for y in range(3)]
    for x in range(0,3):
        for y in range(0,3):
            gameBoardCopy[x][y] = gameBoard[x][y]
    for row in range (0,3):
        for column in range (0,3):
            if gameBoardCopy[row][column] == int(0):
                gameBoardCopy[row][column]  = int(2)
                gameBoardCopy[row][column] = Score(gameBoardCopy, row, column)
                #print(gameBoardCopy[row][column])
    """for x in range(0,3):
        print (gameBoardCopy[x])"""
    return gameBoardCopy
    """
    print("this is the copy")
    for x in range(0,3):
        print(gameBoardCopy[x])
    highestScore = int(0)
    rowColArray = {"row": int(0),"col": int(0)}
    for x in range(0,3):
        for y in range(0,3):
            if gameBoardCopy[x][y] > highestScore and gameBoard[x][y] == int(0):
                rowColArray["row"] = int(x)
                rowColArray["col"] = int(y)
                highestScore = gameBoardCopy[x][y]
    
    return rowColArray
    """
def Score (gameBoardCopy, row, column):
    score = int(0)
    scoreMidMan = int(0)
    for x in range(0,3):
        if gameBoardCopy[x][column] == gameBoardCopy[row][column]:
            score = score + 1
            if score == 3:
                score = 1000
    for y in range(0,3):
        if gameBoardCopy[row][y] == gameBoardCopy[row][column]:
            scoreMidMan = scoreMidMan + 1
            if scoreMidMan == 3:
                score = 1000
    score = score - 1 + scoreMidMan - 1
    scoreMidMan = int(0)
    if gameBoard[0][0] == gameBoard[row][column] or gameBoard[2][2] == gameBoard[row][column]:
        for z in range (0,3):
            if gameBoard[z][z] == gameBoard[row][column]:
                scoreMidMan = scoreMidMan + 1
                if scoreMidMan == 3:
                    score = 1000
    score = score + scoreMidMan
    scoreMidMan = int(0)
    if gameBoard[2][0] == gameBoard[row][column] or gameBoard[0][2] == gameBoard[row][column]:
        for z in range (0,3):
            if gameBoard[2 - z][0 + z] == gameBoard[row][column]:
                scoreMidMan = scoreMidMan + 1
                if scoreMidMan == 3:
                    score = 1000
    score = score + scoreMidMan + Defense(gameBoardCopy, row, column)
    scoreMidMan = int(0)
    return score

def Defense(gameBoardCopy, row, column):
    score = int(0)
    scoreMidMan = int(0)
    isBlocked = False
    if gameBoardCopy[row][column] == int(1):
        oppPlayer = int(2)
        myPlayer = int(1)
    elif gameBoardCopy[row][column] == int(2):
        oppPlayer = int(1)
        myPlayer = int(2)
    if gameBoardCopy[0][column] == gameBoardCopy[row][column] or gameBoardCopy[2][column] == gameBoardCopy[row][column]:
        for x in range(0,3):
            if gameBoard[x][column] == oppPlayer:
                scoreMidMan = scoreMidMan + 1
                """if scoreMidMan == 2:
                    scoreMidMan = 500
                    print("col")"""
            if gameBoard[x][column] == myPlayer:
                isBlocked = True
        if scoreMidMan == 2 and isBlocked == False:
            score = 500
    scoreMidMan = int(0)
    isBlocked = False
    if gameBoardCopy[row][0] == gameBoardCopy[row][column] or gameBoardCopy[row][2] == gameBoardCopy[row][column]:
        for y in range(0,3):
            if gameBoard[row][y] == oppPlayer:
                scoreMidMan = scoreMidMan + 1
                """if scoreMidMan == 2:
                    scoreMidMan = 500
                    print("row")"""
            if gameBoard[row][y] == myPlayer:
                isBlocked = True
        if scoreMidMan == 2 and isBlocked == False:
            score = 500
    isBlocked = False
    #score = score + scoreMidMan
    scoreMidMan = int(0)
    if gameBoardCopy[0][0] == gameBoardCopy[row][column] or gameBoardCopy[2][2] == gameBoardCopy[row][column]:
        for z in range (0,3):
            if gameBoard[z][z] == oppPlayer:
                scoreMidMan = scoreMidMan + 1
                """if scoreMidMan == 2:
                    scoreMidMan = 500
                    print("diag down")"""
            if gameBoard[z][z] == myPlayer:
                isBlocked = True
        if scoreMidMan == 2 and isBlocked == False:
            score = 500
    #score = score + scoreMidMan
    isBlocked = False
    scoreMidMan = int(0)
    if gameBoardCopy[0][2] == gameBoardCopy[row][column] or gameBoardCopy[2][0] == gameBoardCopy[row][column]:
        for z in range (0,3):
            if gameBoard[2 - z][0 + z] == oppPlayer:
                scoreMidMan = scoreMidMan + 1
                """if scoreMidMan == 2:
                    score = 500
                    print("diag up")"""
            if gameBoard[2 - z][0 + z] == myPlayer:
                isBlocked = True
        if scoreMidMan == 2 and isBlocked == False:
            score = 500
    #score = score + scoreMidMan 
    scoreMidMan = int(0)
    """print("this is the Defense score")
    print(score)"""
    #print(oppPlayer)
    return score
    #this will produce a score for the board



gameBoard = [[int(0) for x in range(3)] for y in range(3)]

for x in range(0,3):
    print(gameBoard[x])
win = False
draw = False
while win == False and draw == False:
    #Player 1 Method
    player1 = int(1)
    print("Player 1 select your move")
    rowColArrayOne = AIplayer(gameBoard)
    
    column = int(input("select column"))-1
    row = int(input("select row"))-1
    
    #column = int(rowColArrayOne["col"])
    #row = int(rowColArrayOne["row"])
    gameBoard[row][column] = int(1)
    
    for x in range(0,3):
        print(gameBoard[x])
    win = checkWin(gameBoard, row, column)
    draw = checkDraw(gameBoard, win)
    if win or draw:
        break
    #Player 2 Method
    player2 = int(2)
    print("Player 2 select your move")
    rowColArray = AIplayer(gameBoard)
    column = int(rowColArray["col"])
    row = int(rowColArray["row"])
    gameBoard[row][column] = int(2)
    for x in range(0,3):
        print(gameBoard[x])
    win = checkWin(gameBoard, row, column)
    draw = checkDraw(gameBoard, win)
if win == True:
    print("Congratulations to the winner")
else:
    print("It's a draw")
    