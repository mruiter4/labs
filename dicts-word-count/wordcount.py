import string

def count_words(filename):
    """count the # of times each word appears in the file"""
    word_count = {}

    file = open(filename)
    
    for line in file:
        line = line.rstrip()
        word_list = line.split()

        for word in word_list:
            word = word.strip(string.punctuation)
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f'{word} : {count}')

    file.close()

    