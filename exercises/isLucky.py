def isLucky(n):
    number_list = str(n)
    half = int(len(number_list)/2)
    return sum([int(item) for item in number_list[:half]]) == sum([int(item) for item in number_list[half:]])


print(isLucky(1551))