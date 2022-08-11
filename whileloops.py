# While loops

i = 1
while i < 6:
    print(i)
    i += 1

# Note: remember to increment i, or else the loop will continue forever.

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")