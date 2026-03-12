ss = input()
a,b = map(int, input().split())
print(ss[:a]+ss[b+1:])
