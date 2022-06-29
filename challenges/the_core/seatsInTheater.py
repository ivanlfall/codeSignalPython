def seatInTheater(nCols, nRows, col, row):
    seats = []
    _row = [1 for item in range(0,nRows)]
    for i in range(0, nCols):
        for j in range(0, nRows):
            _row[j] = i
        seats.append(_row)
        # print()

    # for i in range(0, nCols):
    #     for j in range(0, nRows):
    #         print(str(1) + '\t', end='')
    #     print()

    # print(seats)

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            print(str(seats[i][j]) + '\t', end='')
        print()

seatInTheater(10,11,1,1)