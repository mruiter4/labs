import string
import sys


def count_words(filename):
    """count the # of times each word appears in the file"""
    word_count = {}

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            word_list = line.split()

            for word in word_list:
                word = word.strip(string.punctuation)
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

def print_words(word_count):
    for word, count in word_count.items():
        print(f'{word} : {count}')

filename = sys.argv[1]
word_counts = count_words(filename)
print_words(word_counts)

    