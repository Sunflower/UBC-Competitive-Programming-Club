n = int(input())

cir = [int(x) for x in input().split(' ')]

output = []

coins = [0]*n
for c in cir:
    coins[c-1] = c
        
    looks = sum([1 for i,j in zip(coins, sorted(coins)) if (j and i!=j)]) + 1
    output.append(str(looks))
output = ['1'] + output

print(' '.join(output))