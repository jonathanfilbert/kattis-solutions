fl = int(input())
sl = int(input())

print((sl < 0) * 2 + ((sl < 0) ^ (fl < 0)) + 1)
