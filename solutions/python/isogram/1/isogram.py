def is_isogram(string):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    string = string.lower()
    letters = [ch for ch in string if ch in alphabets]
    return len(set(letters)) == len(letters)
            
        
