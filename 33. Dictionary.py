dic = {
    344: "Priyank",
    122: "SUbham",
    253: "Raju", 
    25: "Mohan",
    99: "Champu"
}
print(dic)
print(dic[344])
print(dic.get(344)) #Will not throw an error even if key doesn't exists

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(key)
    print(dic[key])

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())

for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {dic[key]}")