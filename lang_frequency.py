import os.path
import sys
import string
from collections import Counter


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as text_file:
            return text_file.read()
    else:
        return None


def get_most_frequent_words(text):
    number_of_words = 10
    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans({char: None for char in string.punctuation}))
    return Counter(text.split()).most_common(number_of_words)


if __name__ == '__main__':
    text_data = load_data(sys.argv[1])
    if text_data:
        for word in get_most_frequent_words(text_data):
            print(word[0], word[1])
    else:
        print("Не удалось прочитать файл")
