def has_digit(password):
    return any(letter.isdigit() for letter in password)


def is_very_long(password):
    return len(password) > 12


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


password = input("Введите пароль: ")
score = 0
checks = [is_very_long, has_digit, has_letters, has_upper_letters, has_symbols]
score = 2 * sum(check(password) for check in checks)

if not any(check(password) for check in checks):
    print("Пароль слишком простой")

print("Рейтинг пароля:", score)
