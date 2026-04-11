n = int(input())

solved = {}
wrong = {}

accepted_count = 0
total_penalty = 0

for _ in range(n):
    time_str, problem, verdict = input().split()
    
    # convert time to minutes
    h, m = map(int, time_str.split(':'))
    t = h * 60 + m
    
    # initialize if not seen
    if problem not in solved:
        solved[problem] = False
        wrong[problem] = 0
    
    # ignore if already solved
    if solved[problem]:
        continue
    
    if verdict == "OK":
        solved[problem] = True
        accepted_count += 1
        total_penalty += t + 20 * wrong[problem]
    
    elif verdict != "CE":
        wrong[problem] += 1

print(accepted_count, total_penalty)
