def average(number_list):
    if len(number_list) == 0:
        return 0
    return sum(number_list) // len(number_list)


score_list = [70, 60, 90, 80, 100]
avg = average(score_list)
print(avg)

score_list = []
avg = average(score_list)
print(avg)
