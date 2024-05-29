ep1 = {
    122: 45,
    123: 89,
    567: 96,
    879: 66
}
ep2 = {
    222: 88,
    125: 67
}

ep1.update(ep2)
print(ep1)

ep2.clear()
print(ep2)

empt = {}
print(empt)

ep1.pop(122)
print(ep1)

ep1.popitem() # Last key value pair remove
print(ep1)

del ep2
# print(ep2) Will throw an error because ep2 has been deleted

del ep1[567] #Deletes specific key value pair
print(ep1)