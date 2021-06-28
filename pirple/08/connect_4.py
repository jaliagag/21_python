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

while(counter < 49):
    print("")

    insertPiece = int(input("Which column are you going to put your piece? "))
    
    if player == 1:
        if leField[insertPiece] == " ":
            leField[insertPiece] = "X"
            player = 2

    if player == 2:
         if leField[insertPiece] == " ":
            leField[insertPiece] = "O"
            player = 1

    counter += 1 

    drawField(leField)

# winning conditions


