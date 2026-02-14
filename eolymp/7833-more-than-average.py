n = int(input())

lst = list(map(int, input().split()))
summ = 0
for i in lst:
    summ = summ+i

avg = summ/len(lst)
lst2 = []
x = 0
for i in lst:
    if i>avg:
        lst2.append(i)
        x+=i

print(x, len(lst2))
