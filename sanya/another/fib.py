f1 = 0
f2 = 1

n = 8
if n > 2:
    i = 2
    while i < n + 1:
        f1, f2 = f2, f1 + f2
        i += 1

    print(f1, f2)