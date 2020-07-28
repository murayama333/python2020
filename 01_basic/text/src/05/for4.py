for i in range(1, 10):
    for j in range(1, 10):
        if i == 5:
            break
        elif j == 5:
            continue
        print(i * j, end=" ")
    print()
