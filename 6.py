

def main():
    score = 0
    password = input('Введите пароль: ')
    func = [
        has_digit(password),
        has_lower_letters(password),
        has_upper_letters(password),
        is_very_long(password),
        has_symbols(password)
    ]
    for i in func:
        if i:
            score += 2
    print('Рейтинг пароля:', score)


def has_digit(password):
    return any(i.isdigit() for i in password)


def is_very_long(password):
    return len(password) >= 12


def has_letters(password):
    return any(i.isalpha() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isalpha() and not i.isdigit() for i in password)


if __name__ == '__main__':
    main()
