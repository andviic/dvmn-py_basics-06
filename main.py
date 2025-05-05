def is_very_long(password):
    return len(password) >= 12


def has_difgit(password):
    return any(digit.isdigit() for digit in password)


def has_lower_letters(password):
    return any(lower_letter.islower() for lower_letter in password)


def has_upper_letters(password):
    return any(upper_letter.isupper() for upper_letter in password)


def has_symbols(password):
    return any(not symbol.isalpha() and not symbol.isdigit()
               for symbol in password)


def main():
    password = input('Введите пароль: ')

    functions = [
        is_very_long,
        has_difgit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]

    score = 0
    for password_strength in functions:
        if password_strength(password):
            score += 2

    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()
