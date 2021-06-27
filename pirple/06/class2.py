blackShoes = {
        42: 2,
        41: 3,
        40: 3,
        39: 1,
        38: 0
        }

print(blackShoes)
print("use input 0 to exit")

while(True): # infinite loop same as True == True):
    purchaseSize = int(input("which shoe size would you like to buy?\n"))
    if purchaseSize == 0:
        print("bye!")
        break
    elif purchaseSize not in blackShoes:
        print("apologies, we don't have shoe size", purchaseSize)
    elif blackShoes[purchaseSize] > 0:
        print("success!")
        blackShoes[purchaseSize] -= 1
    elif blackShoes[purchaseSize] == 0:
        print("apologies, we are out of stock for size", purchaseSize)
        #purchaseSize
    print("stock:",blackShoes)
 


