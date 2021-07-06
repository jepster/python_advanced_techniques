import random

"""Generate an infinite stream of successively larger random lists."""


def generate_cases():
    cases = []

    for num in range(0,10):
        cases.append(random.randint(0, 99))

    yield cases

if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)