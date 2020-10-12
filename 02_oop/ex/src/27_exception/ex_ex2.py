while True:
    try:
        x = int(input("Input: "))
        print(x)
        break
    except ValueError as e:
        pass
