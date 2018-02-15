n = int(input())
ro = int(input())
re = int(input())
oe = int(input())

house = 0 # 0 = Rabbit, 1 = Owl, 2 = Eeyore
distance = 0
while (n>1):
    if (house==0):
        if ro < re:
            distance += ro
            house = 1
        else:
            distance += re
            house = 2
    elif (house==1):
        if ro < oe:
            distance += ro
            house = 0
        else:
            distance += oe
            house = 2
    elif (house==2):
        if re < oe:
            distance += re
            house = 0
        else:
            distance += oe
            house = 1 
    n -= 1
    
print(distance)