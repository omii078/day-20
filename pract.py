rows = 5
for i in range(1,6):
    for j in range(rows-i):
        print(" ", end=" ")
    for n in range(2 * i - 1):
        print("*", end=" ")
    print()
