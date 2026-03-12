ss = input()
a,b = map(int, input().split())

count = b-a+2
print(count)
for i in range(count-2):
    print(ss[a:b])
    a+=1
    

