tup = (1, 5, 6, 25, 668, 1, 58, "Blue", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[3])
print(tup[4])

if 668 in tup:
    print("yes 668 is present in tuple")
else:
    print("No, it's not present in tuple")

tup2 = tup[1:4]
print(tup2)