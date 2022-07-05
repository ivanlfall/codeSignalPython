def maxMultiple(divisor, bound):
    max = 0
    for number in range(divisor, bound+1):
        if number % divisor == 0:
            if number > max:
                max = number

    return max

print(maxMultiple(3,10))