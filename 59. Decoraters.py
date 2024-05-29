def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("Hello world")

def sum(a, b):
    print(a + b)


hello()
# greet(hello)() You can decorate hello() function like this well
greet(sum)(5, 6)