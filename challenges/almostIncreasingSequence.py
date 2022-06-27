def almostIncreasingSequence(sequence):
    counter = 0
    aux_sequence = [sequence[index] for index in range(1, len(sequence)-1)
                    if (sequence[index] > sequence[index-1]) and (sequence[index]< sequence[index+1])]

    if sequence[0] not in aux_sequence:
        aux_sequence.insert(0, sequence[0])

    # for index in range(1, len(sequence)-1):
    #     if (sequence[index] <= sequence[index-1]) and (sequence[index-1] < sequence[index+1]):
    print(aux_sequence)
    return True if len(sequence) - len(aux_sequence) <= 1 else False

print(almostIncreasingSequence([1, 2, 1, 2]))