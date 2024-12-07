tuloy = True
num = 0

while tuloy:
    ask = input("Do you wish to create a new triangle (yes or no) -> ")

    if ask.lower() == "no":
        print("Program / Loop Terminated")
        break
    elif ask.lower() == "yes":
        num += 1
        for x in range(1,6):
            for a in range(1,num + 4):
                for y in range(1,x+1):
                    print(y,end=" ")
                for z in range(6,x,-1):
                    print(" ",end=" ")
            print()
        continue
else:
    print("Invalid answer, pls only answer 'yes' or 'no'")
    



