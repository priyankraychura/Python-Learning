marks = [25, 36, 85, 95, 74, 25, 44]

# index = 0
# for mark in  marks:
#     print(mark)
#     if(index == 3):
#         print("Priyank great!")
#     index += 1

for index, mark in  enumerate(marks, start = 1):
    print(f"Index: {index}, Value: {mark}")
    if(index == 3):
        print("Priyank great!")

