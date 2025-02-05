text = 'Seneca'
offset = 0
length = len(text)
while offset < length:
    print(offset, text[offset])
    offset += 1

text = "Seneca"
for letter in text:
    print(letter)

def find(text, char):
    for letter in text:
        if letter == char:
            return True
    return False

if __name__ == '__main__':
    s1 = 'Seneca'
    print(s1, 'contains letter s? ->', find(s1, 's'))
    print(s1, 'contains letter S? ->', find(s1, 'S'))

    s1 = 'Seneca'
    print(s1, 'contains letter s? ->', 's' in s1)
    print(s1, 'contains letter S? ->', 'S' in s1)

def is_vowel(char):
    return char in 'aeiou'

if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
            vowel_count += 1
    print('There are', vowel_count, 'vowel(s) in', text)

def is_digits(sobj):
    for char in sobj:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')