ss = input()

first=-1
last=-1
for i in range(0, len(ss)):
    if ss[i]==" ":
        first=i
        break
for i in range(len(ss)-1,-1,-1):
    if ss[i]==" ":
        last=i
        break
if first==-1 or last==-1:
    print(-1)
else:
    print(first, last)
