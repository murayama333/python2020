import io

try:
    with open("not_exist.txt", "w") as f:
        print(f.read())
except io.UnsupportedOperation as e:
    print(e)
finally:
    print("end")
