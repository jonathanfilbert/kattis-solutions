fl = int(input())
sl = int(input())

if (fl > 0) & (sl > 0):
    print(1)
elif (fl > 0) & (sl < 0):
    print(4)
elif (fl < 0) & (sl < 0):
    print(3)
elif (fl < 0) & (sl > 0):
    print(2)