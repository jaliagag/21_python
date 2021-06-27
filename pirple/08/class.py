scores = []

for i in range(5):
    currentScore = int(input("please enter the score "+str(i+1)+": "))
    # could be float rather than int
    scores.append(currentScore)

print(scores)

