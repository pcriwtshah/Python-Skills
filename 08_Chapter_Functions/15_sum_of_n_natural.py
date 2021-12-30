def sum_natural(n):
    while n > 0:
        return (n + int(sum_natural(n - 1)))

a = sum_natural(5)
print(a)