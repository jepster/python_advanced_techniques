import collections


def count_unique_words(filename):
    words = collections.Counter()

    with open(filename) as f:
        for line in f:
            words.update(line.split())

    for word, count in words.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')