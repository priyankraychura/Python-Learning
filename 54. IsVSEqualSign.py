# is compares the direct location of the variable
# == comapres the value 

#LISTS
a = [1, 25, 69] #LISTS ARE MUTABLE
b = [1, 25, 69]
print(a is b)
print(a == b)

c = (1, 5, 9) #TUPLE IS IMMUTABLE
d = (1, 5, 9)
print(c is d)
print(c == d)
