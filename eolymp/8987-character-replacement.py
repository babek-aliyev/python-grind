ss = input()
new = []
for i in ss:
    if i=="a":
        new.append("b")
    elif i=="b":
        new.append("a")
    else:
        new.append(i)

for i in new:
    print(i, end="")
