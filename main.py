import re
from constants import WORD_FREQUENCY_HEADER, WORD_FREQUENCY_SEPARATOR,INPUT_HEADER


def get_word_counts(text):

    words = re.findall(r'\b\w+\b', text.lower())
    counts = {word: words.count(word) for word in set(words)}

    return counts


def print_word_counts(word_counts):
    print(WORD_FREQUENCY_HEADER)
    print(WORD_FREQUENCY_SEPARATOR)
    for word, count in word_counts.items():
        print(f"{word} {count}")


def read_text_file(filename):

    with open(filename, 'r') as file:
        data = file.read()
    return data


def main():

    filename = input(INPUT_HEADER)

    data = read_text_file(filename)

    word_counts = get_word_counts(data)

    print_word_counts(word_counts)


if __name__ == '__main__':
    main()
