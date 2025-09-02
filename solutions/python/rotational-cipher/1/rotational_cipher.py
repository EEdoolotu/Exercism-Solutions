def rotate(text, key):
    result =""
    for ch in text:
        if ch.isupper():
            result+= chr((ord(ch) - 65 + key) % 26 + 65 )
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result 
