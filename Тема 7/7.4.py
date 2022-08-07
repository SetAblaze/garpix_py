def word_counter(file, word):
    counter = 0
    with open(file, encoding='utf-8', mode='r') as f:
        output_file = f.readlines()
        for line in output_file:
            counter += line.count(word)
    print(f'Вхождений слова {word} в файле: {counter} ')

word_counter(r'./test_data/data2', 'текс')