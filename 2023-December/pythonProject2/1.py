for num in range(100, 1000):
    temp = num
    sum = 0
    while temp:
        sum += (temp % 10) ** 3
        temp //= 10
    if sum == num:
        print(num)