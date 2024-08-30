number = int(input('enter the number of rows:'))
for R in range(number):
    for C in range(number - R - 1):
        print("", end="")
    for C in range(C + 1):
        print('*',end="")
    print()
