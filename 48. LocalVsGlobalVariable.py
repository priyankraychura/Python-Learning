x = 4
print(x)

def hello():
    global x
    x = 5
    print("Hello Priyank")
    print(f"Local x is {x}")

print(f"Global x is {x}")
hello()
print(f"Global x is {x}")
