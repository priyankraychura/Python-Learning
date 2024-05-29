countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[1] = "Finland"
countries = tuple(temp)
print(countries)

con = ("India", "Afghanistan1", "Bangladesh", "Shrilanka")
con2 = ("Vietnam", "Pakistan", "China")
southEastAsia = con + con2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
print("Count of 3 iin tuple1 is: ", res)
index = tuple1.index(31)
index2 = tuple1.index(3, 4, 8)
print(index)
print(index2)

length = len(tuple1)
print(length)