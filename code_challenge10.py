for x in range(0, 5):
    for y in range (5, x, -1):
       print(" ", end=" " )
    for z in range (0, x*2):
        print("*", end=" " )
    print()
for a in range(5, 0, -1):
    for b in range (5, a, -1):
       print(" ", end=" " )
    for c in range (0, a*2):
        print("*", end=" " )
    print()