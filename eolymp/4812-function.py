import sys
import math

for line in sys.stdin:
    x = float(line.strip())
    
    part1 = math.sin(x)
    part2 = math.sqrt(math.log(3 * x) / math.log(4))
    part3 = math.ceil(3 * math.exp(x))
    
    result = part1 + part2 + part3
    
    print(f"{result:.6f}")
