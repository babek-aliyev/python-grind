n = int(input())
cond1 = n%2==1
cond2 = n>0 and 100<=n<=999

if cond1 or cond2:
    print("YES")
else:
    print("NO")
