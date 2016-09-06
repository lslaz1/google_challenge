def answer(x):
    sum = 0

    for n in str(x):
        sum += int(n)

    if sum < 10:
        return sum
    else:
        return answer(sum)
