def areSimilar(a,b):
    aux_item_a, aux_item_b = (None, None)
    counter = 0

    for item_a, item_b in zip(a, b):
        if item_a == item_b:
            continue
        else:
            if aux_item_a == None:
                if counter == 1:
                    return False
                counter += 1
                aux_item_a, aux_item_b = (item_a, item_b)
                continue
            else:
                if (item_b == aux_item_a and item_a == aux_item_b):
                    aux_item_a, aux_item_b = (None, None)
                    continue
                else:
                    return False

    return True if aux_item_a == None else False

print(areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))