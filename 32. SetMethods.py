s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
print(cities)

# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

cities3 = cities.difference(cities2)
print(cities3)

print(cities.isdisjoint(cities2))

c1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
c2 = {"Seoul", "Kabul"}
c3 = {"Tokyo", "Madrid"}
print(c1.issuperset(c2))
print(c1.issuperset(c3))
print(c3.issubset(c1))

cities.add("Helsinki")
print(cities)
cities.remove("Tokyo")
print(cities)
cities.discard("Tokyo") #Won't raise an error even if the "Tokyo" is already been removed and doesn't exists
print(cities)

item = cities.pop()
print(cities)
print(item)

del c1
# print(c1) Will throw an error because we have already deleted c1 list

c2.clear()
print(c2)

if "Delhi" in cities:
    print("Delhi is present")
else:
    print("Delhi is not there")