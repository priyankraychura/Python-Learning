import os

files = os.listdir("clutteredFolder")

i = 1
for file in files:
    if(file.endswith(".jpg")):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}")
        i = i + 1