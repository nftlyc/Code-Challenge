tuloy = True
total = 0
ilan = 0
while tuloy:
    namba = int(input("Pls enter a number --> "))
    if namba == 0:
        print("Loop has now terminated")
        print(f"You have entered {ilan} numbers")
        print(f"The sum of all the numbers given is {total}")
        break
    ilan += 1
    total += namba





