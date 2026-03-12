grades = input()

count2 = 0
count5 = 0

for i in grades:
    if i=="2":
        count2+=1
    else:
        count5+=1

if count2>count5:
    print(2)
elif count2==count5:
    print("=")
else:
    print(5)
