import sys

nums = []
for line in sys.stdin:
    nums.extend(map(int, line.split()))

sum = 0
for i in nums:
    sum+=i

print(sum)
