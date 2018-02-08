people = []
N = int(input())
while N:
    name, speed = raw_input().split()
    if not name:
        break
    people.append((name, int(speed)))
    N -= 1
     
f = people[0][1]
p = people[0][0]
for peep in people:
    if peep[1] > f:
        f = peep[1]
        p = peep[0]
print p