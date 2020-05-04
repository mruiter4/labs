def count_words(filename):
    """count the # of times each word appears in the file"""
    word_count = {}

    file = open(filename)
    
    for line in file:
        line = line.rstrip()

        word_list = line.split(" ")

        for word in word_list:
            word_count[word] = word_count.get(word, 0) + 1

    file.close()

  
    for word, count in word_count.items():
        print(f'{word} : {count}')


