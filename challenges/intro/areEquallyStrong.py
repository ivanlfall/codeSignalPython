def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = [yourLeft, yourRight]
    your_friend = [friendsLeft, friendsRight]

    if max(you) == max(your_friend):
        return True if min(you) == min(your_friend) else False

    return False


print(areEquallyStrong(10, 15, 15, 9))