# def double(x):
#     return x*2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y: (x+y)/2

print(double(5))
print(cube(5))
print(avg(15, 25))
print(appl(cube, 5))
print(appl(lambda x: x*x*x, 5))