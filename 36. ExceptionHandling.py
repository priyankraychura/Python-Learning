a = input("Enter the number: ")
print(f"Multiplication tabel of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid Input!")

try:
    num = int(input("Enter an Integer: "))
    list = [6, 3]
    print(list[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index error!")

print("Some important lines of code")
print("End of program")