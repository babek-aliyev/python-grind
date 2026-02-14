n = int(input())
cond1= n%2==0
cond2= n<0 and n%3==0
if cond1 and cond2:
    print("NO")
elif cond1 or cond2:
    print("YES")
else:
    print("NO")

