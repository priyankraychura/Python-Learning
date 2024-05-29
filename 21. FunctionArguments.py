def average(a = 9, b = 1):
    print("The average is " , (a+b)/2)

# average(4, 6)
# average(1, 5)
# average(5)
# average(b=9)
average(b=9, a=21)

def averageNum(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)

# averageNum(5, 6, 9, 12)
avg = averageNum(5, 6, 9, 12)
print("Average is: ", avg)

def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Raychura", lname="Vallabhbhai", fname="Priyank")