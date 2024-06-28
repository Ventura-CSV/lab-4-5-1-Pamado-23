import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    numbers = []

    count = 0

    while count < 5:
        random_number = random.randint(0,100)
        numbers.append(random_number)
        count += 1
    total = 0
    for num in numbers:
        total += num



    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
