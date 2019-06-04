phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

compare = ['o', 'n', ' ', 't', 'a', 'p']

for letter in phrase:
    if letter not in compare:
        plist.remove(letter)



plist.pop()
plist.pop()
plist.pop(3)

plist.insert(2, ' ')
plist.insert(4, 'a')

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

