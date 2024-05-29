def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num-1))
    
num = 7 
print("Number ", num)
print("Factorial: ", factorial(num))