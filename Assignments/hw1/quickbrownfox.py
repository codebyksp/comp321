import string
num_lines = int(input())

for _ in range(num_lines):
    phrase = input()
    phrase_lower = phrase.lower()
    missing_letters = ''
    for char in string.ascii_lowercase:
        if char not in phrase_lower and char not in ['.', ',', '?', '!', '\'', '\"']:
            missing_letters += char
    if missing_letters == '':
        print("pangram")
    else:
        print("missing " + ''.join(sorted(missing_letters))) #no need to sort since we are iterating in alphabetical order