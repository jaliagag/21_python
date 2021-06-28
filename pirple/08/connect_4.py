# connect 4 rules
# 7x7

def drawField(campo):
    for row in range(13): # 0-13
        if row % 2 == 0:
            for column in range(13):  
                if column % 2 == 0: 
                    if column != 12:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-------------")

# max number of plays = 49
counter = 0
# starts player 1
player = 1

# row lists
leField = [
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        ]

# first view of the field
drawField(leField)

while(counter < 49):
    print("")

    insertPiece = int(input("Which column are you going to put your piece? "))
    
    if player == 1:
        pieces_order(inserPiece)
        player = 2

    if player == 2:
        pieces_order(inserPiece)
        player = 1

    counter += 1 

    drawField(leField)


def pieces_order(column):
    for pieces in range(6,-1,-1):
        if leField[pieces][column] == " ":
            if player == 1:
                print("X")
                break
            if player == 2:
                print("O")
                break



# winning conditions




