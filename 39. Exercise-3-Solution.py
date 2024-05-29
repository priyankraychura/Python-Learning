questions = [
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript", "PHP", "None", 4]         
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Questio for  Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}                b.{question[2]}")
    print(f"c. {question[3]}                b.{question[4]}")
    reply = int(input("Enter your answer 1-4 or 0 to Quit: "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
            print("You have won 10000")
        elif(i == 9):
            money = 320000
            print("You have won 320000")
        elif(i == 14):
            money = 70000000
            print("You have won 70000000")
    else:
        print("Wrong Answer!")
        break
    print("\n")

print(f"Your take home money is {money}")
