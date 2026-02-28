str = input()
ans =[]
for c in str:
    if c=='a':
        continue
    else:
        ans.append(c)

for c in ans:
    print(c, end ="")
