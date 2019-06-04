vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'

print(len(word))

for letter in word:
    if letter in vowels:
        print(letter)
