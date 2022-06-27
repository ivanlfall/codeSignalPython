def arrayChange(inputArray):
    counter = 0
    for index in range(1, len(inputArray)):
        if inputArray[index] > inputArray[index - 1]:
            continue
        result = (inputArray[index - 1] + 1) - inputArray[index]
        counter += result
        inputArray[index] += result

    return counter


print(arrayChange([-1000, 0, -2, 0]))