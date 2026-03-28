row = int(input("Row: "))

for i in range(1,10+1):
    for l in range(1,row+1):
        print(f"| {l} x {i} = {l*i}  |", end="  ")
    print()
