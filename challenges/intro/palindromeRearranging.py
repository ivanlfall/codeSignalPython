

def palindromeRearranging(inputString):
    length = len(inputString)
    counter_char = counter = 0
    isUneven = False
    aux = ""

    if length % 2 == 0:
        for char in inputString:
            if char in aux:
                continue
            aux += char
            counter_char = inputString.count(char)
            if counter_char % 2 == 0:
                counter += inputString.count(char)
            else:
                return False
            if counter == length:
                return True
    else:
        for char in inputString:
            if char in aux:
                continue
            aux += char
            counter_char = inputString.count(char)
            if counter_char % 2 == 0:
                counter += inputString.count(char)
            else:
                if isUneven:
                    return False
                isUneven = True
                counter += inputString.count(char)
            if counter == length:
                return True



print(palindromeRearranging("abbcabb"))