def addBorder(picture):
    string_length = len(picture[0])
    external_border = '*' * (string_length + 2)

    for item in picture:
        item = f'*{item}*'

    picture.insert(0,external_border)
    picture.append(external_border)

    return picture


print(addBorder(["abc","ded"]))
