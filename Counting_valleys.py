n = int(input())
steps = input().strip()
num_valleys = 0        # number of valleys
level = 0              # starts at sea level

for d in steps:
    if d == 'U':       # going upslope
        level += 1
    else:              # going downslope
        if level == 0:
            num_valleys += 1
        level -= 1
print (num_valleys)