def arrayMaximalAdjacentDifference(inputArray):
    maximal_difference = 0

    for index in range(len(inputArray) - 1):
        current_difference = abs(inputArray[index] - inputArray[index + 1])
        if current_difference > maximal_difference:
            maximal_difference = current_difference

    return maximal_difference

print(arrayMaximalAdjacentDifference([2, 9, 1, 0]))