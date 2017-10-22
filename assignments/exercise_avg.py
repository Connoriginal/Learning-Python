def score_average():
    average = 0
    count = 0
    count_f = 0
    while True:
        score = input()
        while not score.isdigit():
            score = input()
        score = int(score)
        if score >= 60 and score <= 100:
            average += score
            count += 1
        elif score < 60 and score > 0:
            count_f += 1
        if score == 0:
            break
    print(count)
    if average != 0:
        average = average/count
        print(round(average,1))
    if count_f != 0:
        print(count_f)

score_average()
