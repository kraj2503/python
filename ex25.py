def break_words(stuff):
    """this ftn will break up words for us"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """sort the words"""
    return sorted(words)


def print_first_word(words):
    """print ther first wprd after poping it out"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """print first and last words after poping it of"""
    word = words.pop(-1)
    print(word)


def sort_sentance(sentence):
    """takes in the full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last_sentence(sentence):
    """print first and last word of senctence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """sorts the word and then prints the first and last line"""
    words = sort_sentance(sentence)
    print_first_word(words)
    print_last_word(words)

