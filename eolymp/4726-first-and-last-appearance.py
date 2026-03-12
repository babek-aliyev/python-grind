ss = input()

first = ss.find("f")
last = ss.rfind("f")

if first!=-1:
    print(first, end=" ")
if last!=-1 and last!=first:
    print(last, end=" ")
