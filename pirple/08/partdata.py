
participantNumber = 2
participantData = [] 
registeredPartiticipants = 0

outputFile = open("participantdata.txt","w")

while(registeredPartiticipants < participantNumber):
    tempPartData = []
    name = input("enter name: ")
    tempPartData.append(name)
    country = input("country: ")
    tempPartData.append(country)
    age = int(input("how old are you: "))
    tempPartData.append(age)
    participantData.append(tempPartData)
    print("#################")
    registeredPartiticipants += 1


#print(participantData)

for participant in participantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")


outputFile.close()

# reading data from the file
print("#####################")
print("#####################")

inputFile = open("participantdata.txt", "r")
inputList = []

for line in inputFile:
    tempPart = line.strip("\n").split()
    #print(tempPart)
    inputList.append(tempPart)

    # "max us 21 \n".strip("\n") --> "max us 21 "
    # "max us 21 ".split() --> ["max","us","21"]


print(inputList)

age = {}

for part in inputList:
    tempAge = int(part[-1])
    if tempAge in age:
        age[tempAge] += 1
    else:
        age[tempAge] = 1
#print(age)

oldest = 0
youngest = 100

mostoccurringage = 0
counter = 0

for tempage in age:
    if tempage>oldest:
        oldest = tempage
    if tempage<youngest:
        youngest = tempage
    if age[tempage]>=counter:
        counter = age[tempage]
        mostoccurringage = tempage

print(oldest)

inputFile.close()

