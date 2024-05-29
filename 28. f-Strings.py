letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "Priyank"

# print(letter.format(name, country))
print(letter.format(country, name))

print(f"Hey my name is {name} and i am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.99999))

price = 49.99999
txt = f"For only {price:.2f} dollars!"
print(txt)

txt = f"For only {{price:.2f}} dollars!"
print(txt)
