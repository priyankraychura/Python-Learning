for i in []:
    print(i)
else:
    print("Sorry no i")

for i in range(6):
    print(i)
    if i == 4:
        break # Else condition doesn't execute
else:
    print("Sorry no i")

i = 0
while i < 7:
    print(i)
    i =  i + 1
    if i == 4:
        break # Else condition doesn't execute
else:
    print("Sorry no i")

for x in range(5):
    print("Iteration no {} in for loop".format(x+1))
else:
    print("Else block in loop")

print("out of loop")