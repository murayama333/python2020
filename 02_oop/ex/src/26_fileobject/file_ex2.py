import datetime

file = "datetime2.txt"
now = datetime.datetime.now()
with open(file, "a") as f:
    f.write(f"{now}\n")
