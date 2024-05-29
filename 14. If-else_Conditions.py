age = int(input("Enter your age: "))
print("your age is: ", age)

#Condition operators
# < ,<= ,> ,>= ,== ,!= 
# print(age > 18)
# print(age >= 18)
# print(age < 18)
# print(age <= 18)
# print(age == 18)
# print(age != 18)

if(age > 18):
    print("You can drive")
else:
    print("You cannot drive")
print("out of condition")

applePrice = 20
budget = 200

if(budget - applePrice > 50):
    print("Alexa, add 1kg apple to the cart")
else:
    print("Alexa, do not add apple to the cart")

num = 0
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
elif(num == 999):
    print("Number is special")
else:
    print("Number is positive")

print("I am happy now")

num = 18
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is gereater than 20")
else:
    print('Numeber is zero')