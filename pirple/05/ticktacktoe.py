#  /  / 
# -----
#  /  / 
# -----
#  /  / 
# 

# fixed tick tack toe
#for row in range(5):
#    if row % 2 == 0:
#        print("  |  |  ")
#    else:
#        print("--------")

for row in range(5):
    if row % 2 == 0:
        for column in range(1,6):
            if column % 2 == 1:
                if column != 5:
                    print(" ",end="")#prevents print from creating a new line
                else:
                    print(" ")
            else:
                print("|",end="")
        # print(" | | ")
        #        12345
    else:
        print("-----")
