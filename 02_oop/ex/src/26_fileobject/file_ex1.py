import datetime

file = "datetime.txt"
now = datetime.datetime.now()
with open(file, "w") as f:
    f.write(f"{now}\n")
