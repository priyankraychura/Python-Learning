# READING A FILE
# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
# f = open('myfile2.txt', 'w')
# f = open('myfile2.txt', 'a')
# f.write("Hello world!")
# f.close()

with open('myfile2.txt', 'a') as f:
    f.write("\nSomething new added")