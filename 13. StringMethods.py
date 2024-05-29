# Strings are Immutable
a = "Priyank !! Priyank !!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Priyank", "Pruthvi"))
print(a.split(" "))

blogHeading = "introducntion tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the console"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

print(a.count("Priyank"))

str2 = "welcome to the console!!"
print(str2.endswith("!!"))

print(str2.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man"
print(str1.find("is"))
print(str1.index("is"))

str1 = "welcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome00"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = 'We wish you happy diwali\n'
print(str1)
print(str1.isprintable()) #False because \n is not printable

str1 = "    " #only space
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man"
print(str1.title())