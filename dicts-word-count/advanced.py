import string
import sys
from collections import Counter

def count_words(filename):
    """count the # of times each word appears in the file"""
    with open(filename) as file:
        text = file.read()
        word_list = text.split()

        #word_counts = Counter()
        word_counts = {}

        for word in word_list:
            word = word.strip(string.punctuation)
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts


def sort_alphabetically(word_counts):
    """sort the word_counts dictionary alphabetically"""
    #returns a list
    return sorted(word_counts.items())


def reverse_tuple(word_counts_tuple):
    """reverse order of tuple items"""
    return (word_counts_tuple[1], word_counts_tuple[0])
    

def sort_by_count(word_counts):
    """sort word_counts by count"""
    #return list sorted by count in descending order
    return sorted(word_counts.items(), key=reverse_tuple)[::-1]


def reverse_and_negate_tuple(word_counts_tuple):
    """reverse tuple and negate the count value"""
    return (-word_counts_tuple[1], word_counts_tuple[0])


def sort_by_desc_count_asc_keys(word_counts):
    """sort by counts descending and keys ascending"""
    alpha_sort = sort_alphabetically(word_counts)
    return sorted(word_counts.items(), key=reverse_and_negate_tuple)


def print_words(word_counts):
    """print word:count in dictionary"""
    for word, count in word_counts:
        print(f'{word} : {count}')

filename = sys.argv[1]
word_counts = count_words(filename)
sorted_alphabetically = sort_alphabetically(word_counts)
sort_by_count = sort_by_count(word_counts)
count_alpha_sort = sort_by_desc_count_asc_keys(word_counts)
print_words(count_alpha_sort)



    