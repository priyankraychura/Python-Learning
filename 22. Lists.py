marks = [3, 5, 6, "Priyank", True, 56, 8, 75, 45, 8]
print(marks)
print(type(marks))
print(len(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])
print(marks[len(marks)-3])

if "Priyank" in marks:
    print("Yes")
else:
    print("No")

# Smae thing apply for string as well
if "iya" in "priyank":
    print("Yes")
else:
    print("No")

print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:8:2])

lst = [i for i in range(10)]
print(lst)

lst = [i for i in range(10) if i%2==0]
print(lst)