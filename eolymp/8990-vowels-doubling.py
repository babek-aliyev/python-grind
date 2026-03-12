ss = input()
lst = ['a','e', 'o', 'u', 'y', 'i']
new = ""
for i in ss:
    if i in lst:
        new=new + i + i
    else:
        new+=i
print(new)
