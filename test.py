import random


def main():
    number = random.randint(1,10)
    while True:
        new_number = int(input("Введите число "))
        if new_number > number:
            print('Меньше')
        elif new_number < number:
            print('Больше>')
        else:
            print('Угадали')
            break


if __name__ == "__main__":
    main()
