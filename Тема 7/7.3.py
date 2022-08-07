def longest_word(file):
    max_size_word = ''
    max_size_words_count = 1
    with open(file, encoding='utf-8', mode='r') as f:
        output_file = f.readlines()
        for line in output_file:
            for i in line.split():
                if len(i) >= len(max_size_word):
                    if len(i) == len(max_size_word):
                        max_size_words_count += 1
                    else:
                        max_size_words_count = 1
                        max_size_word = i

        for i in range(max_size_words_count):
            print(max_size_word)

longest_word(r'./test_data/data2')