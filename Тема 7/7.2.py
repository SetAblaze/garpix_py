def read_last(lines, file):
    with open(file, encoding='utf=8', mode='r') as f:
        output_file = f.readlines()
        for i in range(lines):
            print(output_file[len(output_file) - 1 - i])

read_last(4, r'./test_data/data')