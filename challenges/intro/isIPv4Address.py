def isIPv4Address(inputString):

    list = inputString.split('.')
    if len(list) != 4:
        return False

    for item in list:
        if (item.startswith('0')) and (len(item) > 1):
            return False
        if (not item.isdigit()) or ((int(item) > 255) or (int(item) < 0)):
            return False
    return True

print(isIPv4Address('00.16.254.5'))