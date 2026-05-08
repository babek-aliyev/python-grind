lst = []
n = int(input())
for line in range(0,n):
    h,m,s = map(int, input().split())
    lst.append((h,m,s))

sorted_list = sorted(lst, key=lambda x: (x[0], x[1], x[2]))
for h,m,s in sorted_list:
    print(h,m,s)
