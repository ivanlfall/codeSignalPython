def almostIncreasingSequence(sequence):
    index = 0
    counter = 0

    if (sequence[-1] != max(sequence) or sequence.count(max(sequence)) > 1):
        counter += 1
    while index < len(sequence)-1:
        print(f'lista en indice {index} = {sequence}')
        if counter > 1:
            return False
        if sequence[index] >= sequence[index + 1]:
            sequence.pop(index)
            if index >= 1:
                if sequence[index] <= sequence[index - 1]:
                    return False
            counter += 1
        else:
            index += 1
    return True



print(almostIncreasingSequence([1, 1, 2, 3, 4, 4]))

