str = input()
char = input()
str = str.lower()
count = 0
for c in str:
    if c==char:
        count+=1

print(count)
