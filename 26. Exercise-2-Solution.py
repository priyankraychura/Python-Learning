import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<17):
    print("Good afternoon!")
elif(hour>=17):
    print("Good evening!")
