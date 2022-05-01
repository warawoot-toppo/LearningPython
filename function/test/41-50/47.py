def switch_case(word):
    sc_word = ''
    for c in word:
        if c == c.lower():
            sc_word += c.upper()
        else:
            sc_word += c.lower()
    return sc_word

print(switch_case('My Name Is John Doe'))