s = 0

for i in range(1, 500 + 1):
    if i % 2 != 0:
        if i % 3 == 0:
            s = s + i
            i = i + 6
    else:
        i = i + 1
print(s)
