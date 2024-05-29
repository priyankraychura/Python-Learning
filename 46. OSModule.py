import os

if(not os.path.exists("Data")):
    os.mkdir("Data")

# for i in range(0, 5):
#     os.mkdir(f"Data/Day {i+1}")

# for i in range(0, 5):
#     os.rename(f"Data/Day {i+1}", f"Data/Tutorial {i+1}")

folders = os.listdir("Data")
print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Data/{folder}"))

print(os.getcwd())

os.chdir("Data")
print(os.getcwd())
