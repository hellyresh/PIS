from math import fabs
import re

DELIMITER = '.'


# Parsing block
def parse(num_str, base=10):
    if is_invalid(num_str, base):
        raise ValueError('Please enter a correct float number')
    if is_int_str(num_str):
        return int(num_str, base)
    if base == 10:
        return float(num_str)

    is_negative = num_str[0] == '-'
    abs_num_str = num_str.replace('-', '')

    integer_part = abs_num_str.split(DELIMITER)[0]
    fractional_part = abs_num_str.split(DELIMITER)[1]

    digits = map(lambda x: int(x, base), integer_part + fractional_part)
    degrees = range(len(integer_part) - 1, -len(fractional_part) - 1, -1)

    num = 0
    for digit, degree in zip(digits, degrees):
        num += digit * base ** degree

    return (-1 if is_negative else 1) * num


def is_invalid(num_str, base):
    allowed_digits = '0-' + str(base) if base < 10 else '0-9A-' + form_digit(base)

    pattern = re.compile(f'^[+-]?[{allowed_digits}]*([,.][{allowed_digits}]+)?$')
    return not pattern.search(num_str)


def is_int_str(num_str):
    return num_str.count(DELIMITER) == 0


# Formatting block
def form(number, base=10, max_precision=5):
    formatted_number = ('-' if number < 0 else '')
    formatted_number += form_integer_part(number, base)

    if number % 1 != 0:
        formatted_number += DELIMITER
        formatted_number += form_fractional_part(number, base, max_precision)

    return formatted_number


def form_integer_part(number, base):
    integer_part = int(fabs(number))
    if integer_part == 0:
        return '0'
    formatted_str = ''

    while integer_part > 0:
        digit = integer_part % base
        integer_part //= base
        formatted_str = form_digit(digit) + formatted_str

    return formatted_str


def form_fractional_part(number, base, max_precision):
    fractional_part = number % 1
    formatted_str = ''
    current_precision = 0

    while fractional_part != 0 and current_precision < max_precision:
        digit = int(fractional_part * base)
        fractional_part = (fractional_part * base) % 1
        formatted_str += form_digit(digit)
        current_precision += 1

    return formatted_str


def form_digit(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('A') + digit)


def conversion(num, from_base=10, to_base=10):
    return form(parse(num, from_base), to_base)


def main():
    num_str = input(f"Enter integer or float number (delimiter is {DELIMITER}): ").upper()
    from_base_str = input("Enter source base (default 10): ")
    to_base_str = input("Enter destination base (default 10): ")

    from_base = int(from_base_str) if from_base_str != '' else 10
    to_base = int(to_base_str) if to_base_str != '' else 10

    print(f"Our result: {conversion(num_str, from_base, to_base)}")


if __name__ == "__main__":
    main()
