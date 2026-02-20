a,b=map(int, input().split())

armstrong = []

for i in range(a,b+1):
    nums = list(map(int, str(i)))
    if nums[0]**4+nums[1]**4+nums[2]**4+nums[3]**4==i:
        armstrong.append(i)

print(*armstrong)
