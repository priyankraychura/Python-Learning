l = [12, 1, 89, 7, 6, 9, 10, 1]
print(l)
l.append(25)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(10))
print(l.count(1))

m = l # m is reference of l
m[0] = 0
print(l)

a = l.copy()
a[0] = 25
print(l)
print(a)

l.insert(1, 258)
print(l)

m = [900, 1000, 1100]
k = l + m
l.extend(m)
print(l)
print(k)