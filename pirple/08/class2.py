# file = open("filename", "r") # r --> read, w --> write, a --> append, r+ --> read and write
# file.close()

cities = ["london", "paris", "new york", "cordoba"]

citiesFile = open("vacationPlaces","w") # overwrites if the file exists - creates it if it doesn't exist

for spots in cities:
    citiesFile.write(str(spots + ",\n")) # for write function it has to be a string

citiesFile.close()

citiesFile = open("VacationPlaces", "r")

firstLine = citiesFile.readline()
print(firstLine,end="")
secondLine = citiesFile.readline()
print(secondLine)

for line in citiesFile:
    print(line,end="")
    
citiesFile.close()

print("##########tailandia#############")

citiesFile.close()
#finalSpot = "tailandia"

citiesFile = open("VacationPlaces", "a")
#citiesFile.write(finalSpot)
citiesFile.write(input("where to now captain? "))
citiesFile.close()


citiesFile = open("VacationPlaces", "r")
for line in citiesFile:
    print(line,end="")
 
citiesFile.close()

#thewholefile = citiesFile.read()

#print(thewholefile)

#############################################################################################
# another way of opening a file - file get closed automatically

with open("VacationPlaces","r") as archivoCreado:
    for line in archivoCreado:
        print(line)

