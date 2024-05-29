# with open('file.txt', 'r') as f:
#     print(type(f))
#     f.seek(10)

#     print(f.tell())
#     data = f.read(5)
#     print(f.tell())
#     print(data)

with open('sample.txt', 'w') as f:
    f.write("Hello world!")
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())