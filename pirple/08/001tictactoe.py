def drawField(field):
    for row in range(5): # 0-4
        if row % 2 == 0:
            practicalRow = int(row/2)

            for column in range(5): # 0,1,2,3,4
                                    # 0,.,1,.,2
                if column % 2 == 0:
                    practicalColumn = int(column/2)

                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                        #print(" ",end="")
                    else:
                        print(field[practicalColumn][practicalRow])

                else:
                    print("|",end="")
        else:
            print("-----")

#drawField()
counter = 0
player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentField)
while(counter < 9):
    print("players turn (values 1-3):",player)

    moveRow = int(input("enter row: "))
    if moveRow not in [1,2,3]:
        print("error - values 1, 2 or 3")
        break

    moveColumn= int(input("enter column: "))
    if moveColumn not in [1,2,3]:
        print("error - values 1, 2 or 3")
        break

    if player == 1:
        # make move for player 1
        if currentField[moveColumn-1][moveRow-1] == " ":
            currentField[moveColumn-1][moveRow-1] = "X"
            #currentField[moveRow][moveColumn] = "X"
            player = 2
        else:
            print("error - box is NOT empty, please, use your eyes")

    else:
        # make move for player 2
        #currentField[moveRow][moveColumn] = "O"
        if currentField[moveColumn-1][moveRow-1] == " ":
            currentField[moveColumn-1][moveRow-1] = "O"
            player = 1
        else: 
            print("error - box is NOT empty, please, use your eyes")

    counter += 1    
    print(">>>>>>play "+str(counter)+"/9")
    drawField(currentField)

print("The end!")
