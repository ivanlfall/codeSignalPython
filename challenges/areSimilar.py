def areSimilar(a, b):
    result = False
    aux_container = 0
    counter = 0

    if a == b:
        return True
    else:
        if set(a) == set(b):
            for index in range(len(a)-1):
                if a[index] == b[index]:
                    continue
                elif a[index] == b[index+1]:
                    if a[index+1] == b[index]:
                        aux_container = a[index]
                        a[index] = a[index+1]
                        a[index+1] = aux_container
                        counter += 1
                        if counter > 1:
                            return False
                else:
                    return False
            return True
        else:
            return False


print(areSimilar([1, 2, 2], [2, 1, 1]))
