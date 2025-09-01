def is_armstrong_number(number):
    digits = str(number)
    length = len(digits)
    total = sum(int(d) ** length for d in digits)
    return number == total
