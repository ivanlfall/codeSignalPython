def alternatingSums(a):
    team1_weight = 0
    team2_weight = 0

    for index in range(len(a)):
        if index % 2 == 0:
            team1_weight += a[index]
        else:
            team2_weight += a[index]

    return [team1_weight, team2_weight]



print(alternatingSums([50, 60, 60, 45, 70]))