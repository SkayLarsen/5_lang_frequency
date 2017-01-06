import os.path
import sys
import string
import argparse
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_most_frequent_words(text, number_of_words = 10):
    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans({char: None for char in string.punctuation}))
    return Counter(text.split()).most_common(number_of_words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Подсчет наиболее часто встречающихся слов в текстовом файле")
    parser.add_argument('filepath', help='путь к текстовому файлу')
    args = parser.parse_args()
    text_data = load_data(args.filepath)
    if text_data:
        for word, count in get_most_frequent_words(text_data):
            print(word, count)
    else:
        print("Не удалось прочитать файл")
