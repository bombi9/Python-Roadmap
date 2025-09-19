quesAndAnswers = {"What is the chemical symbol for water? ":"h2o", "Which planet is known as the Red Planet? ":"mars", "What is the process by which plants make their food? ":"photosynthesis", "What is the powerhouse of the cell? ":"mitochondria", "What CPU stand for? ":"central processing unit","What GPU stand for? ":"graphics processing unit","What RAM stand for? ":"random access memory"}
finalScore = 0
nQuest = 0

for quest, ans in quesAndAnswers.items():
    nQuest += 1
    userInput = input(quest)
    if ans.lower() == userInput.lower():
        print("Correct!")
        finalScore += 1
    else:
        print("Incorrect!")

print(f"You got {finalScore} Score.")
print(f"You got {round((finalScore / nQuest) * 100 ,2)}%.")
