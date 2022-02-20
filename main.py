import random


def load_words():
    with open('/usr/share/dict/words') as d:
        return [line.rstrip().lower() for line in d.readlines()]


def right_size():
    def f(word):
        return len(word) == 5

    return f


def correct_spot(char, pos):
    def f(word):
        return word[pos] == char

    return f


def wrong_spot(char, pos):
    def f(word):
        return char in word and word[pos] != char

    return f


def doesnt_contain(char):
    def f(word):
        return char not in word

    return f


if __name__ == '__main__':
    words = load_words()
    constraint_list = [
        right_size(),
        # add constraints after putting the guess
    ]

    for constraint in constraint_list:
        words = list(filter(constraint, words))

    print(f"Left with {len(words)} words")
    if len(words) < 10:
        print(f"Here they are: {', '.join(words)}")
    guess = random.choice(words)

    print(f"How about you guess: '{guess}' ?")
