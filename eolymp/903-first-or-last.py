n = int(input())

a = n//100
b = n%10

if a==b:
    print("=")
else:
    print(a if a>b else b)
