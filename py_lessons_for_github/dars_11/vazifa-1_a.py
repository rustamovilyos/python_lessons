with open('write1.txt', 'r') as adds:
    reader = adds.readlines()
    reader[0] = int(reader[0])

    print(reader[0])