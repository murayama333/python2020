scores = (90, 80, 70, 75, 85)
total = 0
for score in scores:
    total += score
count = len(scores)
average = total // len(scores)
print("Sum:", total)
print("Cnt:", count)
print("Avg:", average)