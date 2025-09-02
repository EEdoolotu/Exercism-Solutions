def is_valid(isbn):
    s = isbn.replace("-", "").replace(" ","")
    if len(s) != 10:
        return False
    if not s[:9].isdigit():
        return False
    if not (s[9].isdigit() or s[9] == "X"):
        return False

    digits = [int(ch) for ch in s[:9]]
    check = 10 if s[9] == "X" else int(s[9])
    digits.append(check)
    total = sum((10 - i) * digits[i] for i in range(10))
    return total % 11 == 0

    