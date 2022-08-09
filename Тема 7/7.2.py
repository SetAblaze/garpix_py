def read_last(lines, file):
    with open(file, encoding='utf=8', mode='r') as f:
        last_line = f.readlines()
        for i in range(-1, -lines - 1, -1):
            print(last_line[i])

read_last(4, r'./test_data/data')