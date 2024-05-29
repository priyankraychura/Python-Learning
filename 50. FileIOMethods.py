# f = open('myfile.txt', 'r')

# i = 0
# while True:
#     line = f.readline()
#     i += 1
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in maths is: {m1}")
#     print(f"Marks of student {i} in maths is: {m2}")
#     print(f"Marks of student {i} in maths is: {m3}")
#     print(line)
    
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()