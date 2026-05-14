n = int(input())

freq = {}

for _ in range(n):
    w = input().strip()
    freq[w] = freq.get(w, 0) + 1

best_word = ""
best_count = 0

for w, c in freq.items():
    if c > best_count or (c == best_count and w > best_word):
        best_word = w
        best_count = c

print(best_word, best_count)
