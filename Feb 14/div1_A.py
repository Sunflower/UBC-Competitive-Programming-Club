n = int(input())

sol = []
for i in range(max(n-9*9,0),n):
    str_i = str(i)
    digits = [int(c) for c in str_i]
    if i + sum(digits) == n:
        sol.append(i)

print(str(len(sol)))
for s in sol:
    print(s)