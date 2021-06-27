word = "hello"

letters = []

for w in word:
#    if w == "l":
#        print("yyyeeeeeeeeeahhhhh")
    letters.append(w)

#print(letters)

counter = 1
sum = 0

while (counter <= 1000):
    #print(counter)
    sum = sum + counter # adding all numbers on range
    counter = counter + 1

#print(sum)

#index = 0
letters = ['a', 'b', 'c', 'd', 'e']

#while (index < len(letters)):
#    print(index)
#    print(letters[index])
#    index = index + 1

height = 5000
velocity = 50
time = 0

while (height>0):
    height = height - velocity
    time = time + 1

#print(int(time))

participants = ["jen", "alex", "tina", "joe", "ben"]

position = 1

for name in participants:
    if name == "tina":
#        print("about to break")
        break # end loop
#    print("about to increment")
    position = position + 1

#print(position)

for currentIndex in range(len(participants)):
    if participants[currentIndex] == "joe":
        break

print(currentIndex+1)

for number in range(10):
    if number%3 == 0:
        print(number, "divisible por 3")
    else:
        print(number, "no divisible por 3")
