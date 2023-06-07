import re


def get_word_counts(text):
    '''
    Returns a dictionary of word counts for the given text.
    '''
    words = re.findall(r'\b\w+\b', text.lower())
    counts = {word: words.count(word) for word in set(words)}
    # Using list comprehension to improve readability
    return counts


def print_word_counts(word_counts):
    '''
    Prints word in the required format of the assignment.
    '''
    print("Word" + " " + "Frequency")
    print("-----------------------")
    for word, count in word_counts.items():
        print(f"{word} {count}")


def read_text_file(filename):
    '''
    Reads the text file and returns the data as a string.
    '''
    with open(filename, 'r') as file:
        data = file.read()
    return data



def main():
    '''
    Main function of the program.
    '''
    data = read_text_file('word-count.txt')

    word_counts = get_word_counts(data)
    print_word_counts(word_counts)


if __name__ == '__main__':
    main()
