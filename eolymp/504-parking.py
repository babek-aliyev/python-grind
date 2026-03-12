n = int(input())
for _ in range(n):
    street = input().strip()
    length = len(street)
    can_park = [True]*length
    
    for i, seg in enumerate(street):
        if seg == 'D':
            can_park[i] = False
        elif seg == 'B':
            for j in range(i-2, i+1):
                if 0 <= j < length:
                    can_park[j] = False
        elif seg == 'S':
            for j in range(i-1, i+2):
                if 0 <= j < length:
                    can_park[j] = False
    print(can_park.count(True))
