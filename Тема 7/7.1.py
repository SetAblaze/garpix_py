def read_poem(poem_dir):
    with open(poem_dir, encoding='utf-8', mode='r') as poem:
        for i in range(6):
            print(poem.readline())

read_poem(r'./data')