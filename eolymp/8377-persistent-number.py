import sys

def persistence(n):
    count = 0
    
    while n >= 10:  # while not single digit
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        
        n = prod
        count += 1
    
    return count

for line in sys.stdin:
    n = int(line.strip())
    print(persistence(n))
