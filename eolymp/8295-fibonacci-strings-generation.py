def f(n):
    if n == 0:
        return "a"
    if n == 1:
        return "b"
    return f(n - 1) + f(n - 2)

n = int(input())
print(f(n))
