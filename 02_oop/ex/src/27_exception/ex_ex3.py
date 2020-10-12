try:
    with open("not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
finally:
    print("end")
