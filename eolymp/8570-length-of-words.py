import sys

for line in sys.stdin:
    st = line.split()
    for i in st:
        print(len(i), end=" ")
