ss = input()
pos = 0
cell = {pos}

for i in ss:
    if i=="R":
        pos+=1
    elif i=="L":
        pos-=1
    cell.add(pos)

print(len(cell))
